
#include <Arduino.h>

#define NUM_KEYS 25
#define SOLENOID_ON_MS 35
#define SERIAL_BAUD 115200

static const uint8_t KEY_PINS[NUM_KEYS] = {
    22, 23, 24, 25, 26, 27, 28, 29,
    30, 31, 32, 33, 34, 35, 36, 37,
    38, 39, 40, 41, 42, 43, 44, 45,
    46
};

static const uint8_t KEY_MIDI[NUM_KEYS] = {
    43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58,
    59, 60, 61, 62, 63, 64, 65, 66,
    69
};

struct StrikeEvent {
    unsigned long fire_at_ms;
    uint8_t pin;
    bool active;
};

static StrikeEvent queue[32];
static uint8_t queue_head = 0;
static uint8_t queue_tail = 0;

static unsigned long session_start_ms = 0;
static bool session_active = false;

static int8_t midi_to_key_index(uint8_t note) {
    for (uint8_t i = 0; i < NUM_KEYS; i++) {
        if (KEY_MIDI[i] == note) return (int8_t)i;
    }
    return -1;
}

static void enqueue_strike(uint8_t pin, unsigned long fire_at_ms) {
    uint8_t next = (queue_tail + 1) & 31;
    if (next == queue_head) return;
    queue[queue_tail].pin = pin;
    queue[queue_tail].fire_at_ms = fire_at_ms;
    queue[queue_tail].active = false;
    queue_tail = next;
}

static void process_queue(unsigned long now_ms) {
    uint8_t i = queue_head;
    while (i != queue_tail) {
        StrikeEvent &ev = queue[i];
        if (!ev.active && now_ms >= ev.fire_at_ms) {
            digitalWrite(ev.pin, HIGH);
            ev.active = true;
            ev.fire_at_ms = now_ms + SOLENOID_ON_MS;
        } else if (ev.active && now_ms >= ev.fire_at_ms) {
            digitalWrite(ev.pin, LOW);
            if (i == queue_head) {
                queue_head = (queue_head + 1) & 31;
            }
        }
        i = (i + 1) & 31;
    }
}

static void parse_command(const char *buf) {
    if (buf[0] == 'S') {
        session_start_ms = millis();
        session_active = true;
        Serial.println("OK_START");
        return;
    }
    if (buf[0] == 'X') {
        session_active = false;
        for (uint8_t i = 0; i < NUM_KEYS; i++) {
            digitalWrite(KEY_PINS[i], LOW);
        }
        queue_head = 0;
        queue_tail = 0;
        Serial.println("OK_STOP");
        return;
    }
    if (buf[0] == 'N') {
        if (!session_active) {
            Serial.println("ERR_NO_SESSION");
            return;
        }
        uint32_t offset_ms = 0;
        uint8_t note = 0;
        const char *p = buf + 1;
        while (*p >= '0' && *p <= '9') {
            offset_ms = offset_ms * 10 + (*p - '0');
            p++;
        }
        if (*p != ',') {
            Serial.println("ERR_BAD_CMD");
            return;
        }
        p++;
        while (*p >= '0' && *p <= '9') {
            note = note * 10 + (*p - '0');
            p++;
        }
        int8_t idx = midi_to_key_index(note);
        if (idx < 0) {
            Serial.println("ERR_NOTE_OOR");
            return;
        }
        unsigned long fire_at = session_start_ms + (unsigned long)offset_ms;
        enqueue_strike(KEY_PINS[idx], fire_at);
        Serial.println("OK_N");
        return;
    }
    if (buf[0] == 'P') {
        if (!session_active) {
            Serial.println("ERR_NO_SESSION");
            return;
        }
        uint8_t note = 0;
        const char *p = buf + 1;
        while (*p >= '0' && *p <= '9') {
            note = note * 10 + (*p - '0');
            p++;
        }
        int8_t idx = midi_to_key_index(note);
        if (idx < 0) {
            Serial.println("ERR_NOTE_OOR");
            return;
        }
        enqueue_strike(KEY_PINS[idx], millis());
        Serial.println("OK_P");
        return;
    }
    if (buf[0] == '?') {
        Serial.print("GLOCKWORK_ORANGE v1.0 KEYS=25 BAUD=");
        Serial.println(SERIAL_BAUD);
        return;
    }
    Serial.println("ERR_UNKNOWN");
}

static char rx_buf[64];
static uint8_t rx_pos = 0;

void setup(void) {
    Serial.begin(SERIAL_BAUD);
    for (uint8_t i = 0; i < NUM_KEYS; i++) {
        pinMode(KEY_PINS[i], OUTPUT);
        digitalWrite(KEY_PINS[i], LOW);
    }
    queue_head = 0;
    queue_tail = 0;
    session_active = false;
}

void loop(void) {
    unsigned long now = millis();
    process_queue(now);

    while (Serial.available()) {
        char c = (char)Serial.read();
        if (c == '\n' || c == '\r') {
            if (rx_pos > 0) {
                rx_buf[rx_pos] = '\0';
                parse_command(rx_buf);
                rx_pos = 0;
            }
        } else if (rx_pos < 63) {
            rx_buf[rx_pos++] = c;
        }
    }
}
