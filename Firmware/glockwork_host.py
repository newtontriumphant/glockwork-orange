
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import serial
import serial.tools.list_ports
import mido
import time
import os

BAUD_RATE = 115200
SOLENOID_RANGE_LOW = 43
SOLENOID_RANGE_HIGH = 69
TOTAL_RANGE = SOLENOID_RANGE_HIGH - SOLENOID_RANGE_LOW

def find_ports():
    return [p.device for p in serial.tools.list_ports.comports()]

def clamp_note_to_range(note):
    while note < SOLENOID_RANGE_LOW:
        note += 12
    while note > SOLENOID_RANGE_HIGH:
        note -= 12
    return note

def extract_voices(midi_path, max_voices=2):
    mid = mido.MidiFile(midi_path)
    tpb = mid.ticks_per_beat
    tempo = 500000

    raw_events = []
    for track in mid.tracks:
        abs_tick = 0
        for msg in track:
            abs_tick += msg.time
            if msg.type == "set_tempo":
                tempo = msg.tempo
            if msg.type == "note_on" and msg.velocity > 0:
                time_sec = mido.tick2second(abs_tick, tpb, tempo)
                raw_events.append((time_sec, msg.note, msg.velocity))

    raw_events.sort(key=lambda e: e[0])

    voice_last_time = [None] * max_voices
    scheduled = []

    for t, note, vel in raw_events:
        mapped = clamp_note_to_range(note)
        assigned = False
        for v in range(max_voices):
            if voice_last_time[v] is None or (t - voice_last_time[v]) >= 0.08:
                voice_last_time[v] = t
                scheduled.append((t, mapped))
                assigned = True
                break
        if not assigned:
            oldest = min(range(max_voices), key=lambda v: voice_last_time[v])
            if (t - voice_last_time[oldest]) >= 0.04:
                voice_last_time[oldest] = t
                scheduled.append((t, mapped))

    scheduled.sort(key=lambda e: e[0])
    return scheduled

class GlockworkApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Glockwork Orange — Firmware Controller")
        self.geometry("600x480")
        self.resizable(False, False)
        self.configure(bg="#1a1a1a")

        self.ser = None
        self.playback_thread = None
        self.stop_event = threading.Event()
        self.midi_path = None
        self.scheduled_events = []

        self._build_ui()
        self._refresh_ports()

    def _build_ui(self):
        top = tk.Frame(self, bg="#1a1a1a", pady=12)
        top.pack(fill="x", padx=20)

        tk.Label(top, text="Glockwork Orange", font=("Courier", 18, "bold"),
                 bg="#1a1a1a", fg="#f5a623").pack(side="left")
        tk.Label(top, text="v1.0", font=("Courier", 10),
                 bg="#1a1a1a", fg="#666666").pack(side="left", padx=8, pady=6)

        port_row = tk.Frame(self, bg="#1a1a1a")
        port_row.pack(fill="x", padx=20, pady=4)

        tk.Label(port_row, text="Port:", font=("Courier", 11),
                 bg="#1a1a1a", fg="#cccccc", width=6, anchor="w").pack(side="left")

        self.port_var = tk.StringVar()
        self.port_menu = ttk.Combobox(port_row, textvariable=self.port_var,
                                       font=("Courier", 11), width=28, state="readonly")
        self.port_menu.pack(side="left", padx=4)

        tk.Button(port_row, text="Refresh", font=("Courier", 10),
                  bg="#2a2a2a", fg="#cccccc", relief="flat", bd=0,
                  activebackground="#3a3a3a", activeforeground="#ffffff",
                  command=self._refresh_ports, padx=8, pady=4).pack(side="left", padx=4)

        self.connect_btn = tk.Button(port_row, text="Connect", font=("Courier", 10),
                                      bg="#f5a623", fg="#1a1a1a", relief="flat", bd=0,
                                      activebackground="#d4891a", activeforeground="#1a1a1a",
                                      command=self._toggle_connect, padx=12, pady=4)
        self.connect_btn.pack(side="left", padx=4)

        self.status_dot = tk.Label(port_row, text="●", font=("Courier", 14),
                                    bg="#1a1a1a", fg="#555555")
        self.status_dot.pack(side="left", padx=8)

        file_row = tk.Frame(self, bg="#1a1a1a")
        file_row.pack(fill="x", padx=20, pady=8)

        tk.Label(file_row, text="MIDI:", font=("Courier", 11),
                 bg="#1a1a1a", fg="#cccccc", width=6, anchor="w").pack(side="left")

        self.file_label = tk.Label(file_row, text="No file selected",
                                    font=("Courier", 10), bg="#1a1a1a", fg="#666666",
                                    anchor="w", width=36)
        self.file_label.pack(side="left")

        tk.Button(file_row, text="Browse", font=("Courier", 10),
                  bg="#2a2a2a", fg="#cccccc", relief="flat", bd=0,
                  activebackground="#3a3a3a", activeforeground="#ffffff",
                  command=self._browse_midi, padx=8, pady=4).pack(side="left", padx=4)

        info_frame = tk.Frame(self, bg="#242424", bd=0, relief="flat")
        info_frame.pack(fill="x", padx=20, pady=4)

        self.info_label = tk.Label(info_frame, text="Load a MIDI file to see event summary.",
                                    font=("Courier", 10), bg="#242424", fg="#888888",
                                    anchor="w", padx=10, pady=8, justify="left")
        self.info_label.pack(fill="x")

        ctrl_row = tk.Frame(self, bg="#1a1a1a")
        ctrl_row.pack(fill="x", padx=20, pady=12)

        self.play_btn = tk.Button(ctrl_row, text="Play", font=("Courier", 13, "bold"),
                                   bg="#27ae60", fg="#ffffff", relief="flat", bd=0,
                                   activebackground="#1e8449", activeforeground="#ffffff",
                                   command=self._play, padx=24, pady=8, state="disabled")
        self.play_btn.pack(side="left", padx=4)

        self.stop_btn = tk.Button(ctrl_row, text="Stop", font=("Courier", 13, "bold"),
                                   bg="#c0392b", fg="#ffffff", relief="flat", bd=0,
                                   activebackground="#922b21", activeforeground="#ffffff",
                                   command=self._stop, padx=24, pady=8, state="disabled")
        self.stop_btn.pack(side="left", padx=4)

        self.progress_var = tk.DoubleVar(value=0)
        self.progress = ttk.Progressbar(self, variable=self.progress_var,
                                         maximum=100, length=560, mode="determinate")
        self.progress.pack(padx=20, pady=4)

        self.progress_label = tk.Label(self, text="0.0s / 0.0s",
                                        font=("Courier", 10), bg="#1a1a1a", fg="#555555")
        self.progress_label.pack()

        log_frame = tk.Frame(self, bg="#1a1a1a")
        log_frame.pack(fill="both", expand=True, padx=20, pady=8)

        tk.Label(log_frame, text="Log", font=("Courier", 10),
                 bg="#1a1a1a", fg="#555555").pack(anchor="w")

        self.log_text = tk.Text(log_frame, font=("Courier", 9), bg="#111111",
                                 fg="#33ff33", height=8, state="disabled",
                                 relief="flat", bd=0, wrap="word")
        self.log_text.pack(fill="both", expand=True)

        sb = ttk.Scrollbar(log_frame, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=sb.set)

    def _log(self, msg):
        self.log_text.configure(state="normal")
        self.log_text.insert("end", msg + "\n")
        self.log_text.see("end")
        self.log_text.configure(state="disabled")

    def _refresh_ports(self):
        ports = find_ports()
        self.port_menu["values"] = ports
        if ports:
            self.port_var.set(ports[0])

    def _toggle_connect(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            self.ser = None
            self.status_dot.configure(fg="#555555")
            self.connect_btn.configure(text="Connect")
            self._log("Disconnected.")
            self._update_play_state()
        else:
            port = self.port_var.get()
            if not port:
                messagebox.showerror("Error", "No port selected.")
                return
            try:
                self.ser = serial.Serial(port, BAUD_RATE, timeout=1)
                time.sleep(2)
                self.ser.write(b"?\n")
                resp = self.ser.readline().decode("utf-8", errors="replace").strip()
                self.status_dot.configure(fg="#27ae60")
                self.connect_btn.configure(text="Disconnect")
                self._log(f"Connected to {port}. FW: {resp}")
                self._update_play_state()
            except Exception as e:
                messagebox.showerror("Connection Error", str(e))

    def _browse_midi(self):
        path = filedialog.askopenfilename(
            filetypes=[("MIDI files", "*.mid *.midi"), ("All files", "*.*")]
        )
        if not path:
            return
        self.midi_path = path
        fname = os.path.basename(path)
        self.file_label.configure(text=fname[:36], fg="#cccccc")
        try:
            self.scheduled_events = extract_voices(path, max_voices=2)
            if self.scheduled_events:
                total = self.scheduled_events[-1][0]
                self.info_label.configure(
                    text=f"Events: {len(self.scheduled_events)}    Duration: {total:.2f}s    "
                         f"Note range: G2-A4 (MIDI 43-69)    Voices: 2"
                )
                self.progress_label.configure(text=f"0.0s / {total:.1f}s")
            self._log(f"Loaded: {fname} — {len(self.scheduled_events)} strike events.")
        except Exception as e:
            messagebox.showerror("MIDI Error", str(e))
        self._update_play_state()

    def _update_play_state(self):
        connected = self.ser and self.ser.is_open
        has_midi = bool(self.scheduled_events)
        playing = self.playback_thread and self.playback_thread.is_alive()
        if connected and has_midi and not playing:
            self.play_btn.configure(state="normal")
        else:
            self.play_btn.configure(state="disabled")
        if playing:
            self.stop_btn.configure(state="normal")
        else:
            self.stop_btn.configure(state="disabled")

    def _play(self):
        if not self.ser or not self.ser.is_open:
            messagebox.showerror("Error", "Not connected.")
            return
        if not self.scheduled_events:
            messagebox.showerror("Error", "No MIDI loaded.")
            return
        self.stop_event.clear()
        self.playback_thread = threading.Thread(
            target=self._playback_worker, daemon=True
        )
        self.playback_thread.start()
        self._update_play_state()

    def _stop(self):
        self.stop_event.set()
        if self.ser and self.ser.is_open:
            try:
                self.ser.write(b"X\n")
            except Exception:
                pass
        self._log("Stopped.")
        self.progress_var.set(0)
        self._update_play_state()

    def _playback_worker(self):
        events = self.scheduled_events
        total_time = events[-1][0] if events else 1.0
        try:
            self.ser.write(b"S\n")
            resp = self.ser.readline().decode("utf-8", errors="replace").strip()
            if resp != "OK_START":
                self.after(0, lambda: self._log(f"Unexpected start response: {resp}"))

            t0 = time.perf_counter()

            for i, (t_sec, note) in enumerate(events):
                if self.stop_event.is_set():
                    break
                now = time.perf_counter() - t0
                wait = t_sec - now - 0.001
                if wait > 0:
                    time.sleep(wait)
                if self.stop_event.is_set():
                    break
                offset_ms = int(t_sec * 1000)
                cmd = f"N{offset_ms},{note}\n".encode("ascii")
                try:
                    self.ser.write(cmd)
                    self.ser.readline()
                except Exception as e:
                    self.after(0, lambda e=e: self._log(f"Serial error: {e}"))
                    break
                pct = (t_sec / total_time) * 100.0
                self.after(0, lambda p=pct, t=t_sec: (
                    self.progress_var.set(p),
                    self.progress_label.configure(text=f"{t:.1f}s / {total_time:.1f}s")
                ))

            if not self.stop_event.is_set():
                self.ser.write(b"X\n")
                self.ser.readline()
                self.after(0, lambda: self.progress_var.set(100))
                self.after(0, lambda: self._log("Playback complete."))

        except Exception as e:
            self.after(0, lambda: self._log(f"Playback error: {e}"))
        finally:
            self.after(0, self._update_play_state)

    def on_close(self):
        self.stop_event.set()
        if self.ser and self.ser.is_open:
            try:
                self.ser.write(b"X\n")
                self.ser.close()
            except Exception:
                pass
        self.destroy()

if __name__ == "__main__":
    app = GlockworkApp()
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()
