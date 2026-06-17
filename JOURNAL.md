Made by: @zsharpminor // gh/newtontriumphant // udo funke

Repository link: https://github.com/newtontriumphant/glockwork-orange/

Total hours so far: 5.0

# GLOCKWORK ORANGE - THE JOURNAL

[placeholder, insert finished schem image here]

## [06/13/26 | 2.0 hours]

### Ideation!

Hi and welcome! You're in for a long journ-ey (pun intended); this is where Glockwork Orange's ideation and development begins. After days of procrastinating starting this project, here we are. This is my Outpost project, it better be good.
I began by researching existing robot glockenspiel options, and came accross a [very interesting article](https://magazine.raspberrypi.com/articles/robot-glockenspiel) that had some great ideas. I didn't like the use of fragile lego parts, and felt that a PCB would work a crapton better than a breadboard, though. Additionally, I wanted Glockwork Orange to be chromatic and fully controllable via a desktop app - users should be able to upload ANY midi file and the app should smart-revoice it to be workable in two octaves with up to two voices.

### The Solenoid Hunt!

After I got the idea for my project, I began by researching **solenoids**. Having worked a bit with sols before, they're incredibly hard to work with, especially the sketchy ones you can get from AliExpress for borderline free. I would need a total of 25 (or more!) solenoids for this project, though, so I needed to compromise between quality and operation. I needed a solenoid that could work at a 5V baseline, would be small enough to fit DIRECTLY over the glock, and was cheap enough to order 25 of. I started at AliExpress, and was disappointed. [The cheapest option I could find](https://www.aliexpress.us/item/3256808985836089.html?spm=a2g0o.productlist.main.4.6f1a5647hGMEid&aem_p4p_detail=2026061316291716291396639822860001124144&algo_pvid=035c97c9-8430-4495-90d2-00fa6c58dbd5&algo_exp_id=035c97c9-8430-4495-90d2-00fa6c58dbd5-3&pdp_ext_f=%7B%22order%22%3A%2299%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%215.57%212.29%21%21%2137.50%2115.38%21%40210319b017813933577635532e33a0%2112000048192039233%21sea%21US%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Abaa2c7c7%3Bm03_new_user%3A-29895%3BpisId%3A5000000208023469&curPageLogUid=d7DN6FKFWTEM&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009172150841%7C_p_origin_prod%3A&search_p4p_id=2026061316291716291396639822860001124144_1) with at least 5mm travel and a small enough form factor was already $5.50, plus shipping.

This was a big issue, since I needed a solenoid with a consistent supplier and datasheet. I looked briefly on Alibaba, but the few I were able to find wanted MOQs of 1000 or more. I tried chatting with the sellers, but it was of no avail. Then, I stumbled accross a relatively reputable and consistent [solenoid sold by Sparkfun on behalf of Shenzhen Zonhen Electric Appliances Co., Ltd](https://www.sparkfun.com/solenoid-5v-small.html), a rather reputable Chinese solenoid company.

![solenoid image](https://user-cdn.hackclub-assets.com/019ec355-0b48-7b36-b29f-b75e37176d0d/image.png)

This solenoid had both a sufficient stroke (6mm), a small enough form factor (12x11mm!), and it could even run on 5V, meaning I didn't have to worry about 24V solenoid power supplies. Finally, it also had a [relatively good datasheet](https://cdn.sparkfun.com/datasheets/Robotics/ZHO-0420S-05A4.5%20SPECIFICATION.pdf), meaning it would be an excellent starting point for Glockwork Orange!

### The Glockenspiel Itself!

> Sidenote: in the musical percussion and orchestra community, "glock" is used to abbreviate "glockenspiel" and is in no way related to the firearm brand created by Gaston Glock.

You can't have a self-playing glock without the glock itself! I started by looking for glocks that already had 3D models available, and found to my dismay that the only available 3D models of glockenspiels were either paid or so low-quality that they didn't sufficiently resemble the real product. For that reason, I shifted approaches and asked myself: what's the cheapest glockenspiel that meets all of the criteria I needed (at least 25 keys, chromatic, top/bottom layout, real metal keys, flat) and would arrive reasonably quickly?

![glock pun](https://cdn.hackclub.com/019ec35a-52ce-705f-b4f3-3b5b6ef130c4/screenshot_2026-06-13_at_4.38.47___pm.png)

(no, amazon, i do not want to buy a gun today, thank you very much)

Anyways, I found this [glockenspiel](https://www.amazon.com/Heuyrao-Glockenspiel-Xylophone-Professional-Instrument/dp/B0F62YSCMV/ref=sr_1_9?dib=eyJ2IjoiMSJ9.xXIuJkP0lO2ybZc5wFefF7viDZzLnqAFy-zRRLIncKiI9z1XQBe5vnDwEaJvh4-lEemETv5A9Iv_H9GzxI_ijOotdn-dUEK6KUAk1bTI-IoOedkGLgns2zG6R9cPYtxC2JPVFXIro5T3tR08D-xbuTkvOI1X7EpgcSGwM2jQH5QXTNhia3TWD2NuZoHVwO-ADjHg2lUPgXI-WQbRAAiaoxk9nanujD5h0cdUi04BRVR94nuHRPh__xhzdEHsded7tbk6kTY28EcraHyXKlvcnA8QHibm-m6PDY5qSNchb74.v1u12mPWPUg6rIrebyCte3WHJWoKibMDxJ7vEJwtnDU&dib_tag=se&keywords=glockenspiel%2B25%2Bnote&qid=1781394339&sr=8-9&th=1) that looked decent and [this 3D model](https://sketchfab.com/3d-models/metalofono-cromatico-25-notas-g2-a-g4-f864735df7be4f87af08a44f3913456a) that would work as a mockup! :D

![glockenspiel 3d model](https://cdn.hackclub.com/019ec363-93f9-7481-a6d8-ecdca7ece357/screenshot_2026-06-13_at_4.48.50___pm.png)

Now, onto the fun part: the 3D modeling of the solenoids! :)

## [06/17/26 | 3.0 hours]

### Research

This week, I began by emailing SparkFun about bulk pricing - and got a bit of a discount, saving over $10 on an order of 30 solenoids, which is pretty nice.

Then, I spent some time looking up existing projects, and besides the one I looked at last week, I found two very compelling candidates: https://www.instructables.com/Copper-Pipe-Auto-Glockenspiel/ and https://neil.fraser.name/hardware/glockenspiel/ - both of which used very similar solenoids, and one of which had the genius idea of implementing LEDs for the playing of the keys. This inspired me to add LEDs to my glockenspiel. Additionally, I found some issues, and made a:

### Checklist

- [x] Find a working solenoid
- [x] Find a working glockenspiel
- [ ] 3D model the solenoid holder
- [ ] Schematic for PCB
- [ ] Routing for PCB
- [ ] 3D model the glock holder
- [ ] Find a way to power the solenoids
- [ ] Write a compelling README
- [ ] ship :3

There may be a ways to go, but a good start for today would be to 3D model the solenoid holder and start the PCB schematic.

### 3D Modeling The Solenoid Holder

I began by looking at the datasheet for the specific solenoid I wanted to work with:

![datasheet](https://cdn.hackclub.com/019ed6d3-2d3f-7aaf-8211-2dbbd0a5455d/Screenshot%202026-06-17%20at%2011.23.37%E2%80%AFAM.png)

My first thought? Not as complicated as I expected. The hardest part for me was figuring out which end of the solenoid was the business end.

> Spoiler alert: both ends move. In solenoids, the "striking" end is the end that doesn't have a spring and appears to be flatter. For my purposes, the spring end would have to be container by the holder, since the holder would be bottom-mounted in relation to the glock! :D

![fusion bootup](https://cdn.hackclub.com/019ed6d9-a0ad-7738-bd29-6e411e386cf1/Screenshot%202026-06-17%20at%2011.30.45%E2%80%AFAM.png)

I really need to learn how to use Onshape one of these days... Fusion is eating up my poor Mac's RAM :p

I started by creating a sketch using the datasheet's dimensions. Since it was quite the crappy datasheet, I had to estimate the spring's diameter.

![sketch](https://cdn.hackclub.com/019ed6f1-715c-76f2-af11-e10db7b4b139/Screenshot%202026-06-17%20at%2011.56.45%E2%80%AFAM.png)

Then, I extruded the solenoid holder, added a fillet, and space for the spring to go downward.

![extrude1](https://cdn.hackclub.com/019ed6f1-4ff9-7000-9e7a-e5ad46d852f5/Screenshot%202026-06-17%20at%2011.56.36%E2%80%AFAM.png)

The plan here is for the solenoid to be held down by a dab of hot glue on two corners. I also added a wire holder and some more fillets.

### 3D Modeling The Assembly (Part One!)

I wanted to have a rail that held the solenoids in place, but to get that to work I first needed a glockenspiel model.

It turns out, it's really hard to find a good glockenspiel model that isn't $30. Thankfully, I found this one:

![og](https://cdn.hackclub.com/019ed704-5fb3-7e1a-88d7-e20f1a0c2270/Screenshot%202026-06-17%20at%2012.17.25%E2%80%AFPM.png)

It wasn't perfect, but it would do the job done. After a crap-ton of plane cutting and retexturing, I got a semi-decent version of it into Fusion:

![infusion](https://cdn.hackclub.com/019ed704-fa82-75df-b447-b1a3ab49d971/Screenshot%202026-06-17%20at%2012.18.03%E2%80%AFPM.png)

This would work quite well for my purposes. Onto modeling the bar!

### 3D Modeling The Holder Bar

After some head-bangingly infuriating googles, I finally got a model of the solenoid and the model of the glockenspiel to scale. I also added bars on the sides:

![bars](https://cdn.hackclub.com/019ed718-d897-7542-8177-4a4ca22571cb/Screenshot%202026-06-17%20at%2012.39.45%E2%80%AFPM.png)

Then, I started working on the screws for the holder bar. I figured out that M2x8 and M2x10mm screws would work best for the non-chromatic and chromatic notes of the glock, respectively.

![sketch](https://cdn.hackclub.com/019ed723-87a9-724f-aca0-5072b17a20cd/Screenshot%202026-06-17%20at%2012.51.26%E2%80%AFPM.png)

This might be a mild bit of chaos, but at least the proportions are right! Finally, the holder bar is ready to accept the holders.

![holderbarsketch](https://cdn.hackclub.com/019ed742-0469-77e7-ba3e-78e8cb3f7530/Screenshot%202026-06-17%20at%201.24.43%E2%80%AFPM.png)

It's been three hours now. I'm going to extrude this and take a break to play my *real* instrument of the violin. This is taking too long :p

Anyways, after some Fusion Magic™️ (and changing WAY too many lines to construction lines), enjoy the final extruded version of the holder bar:

![final_bar](https://cdn.hackclub.com/019ed74e-425c-7201-9922-f94ff3b646f6/Screenshot%202026-06-17%20at%201.38.06%E2%80%AFPM.png)

There's a bit of an offset issue - but that can easily be fixed later. See ya tonight! :D

- [x] 3D model the solenoid holder
