Made by: @zsharpminor // gh/newtontriumphant // udo funke
Repository link: https://github.com/newtontriumphant/glockwork-orange/
Total hours so far: 2.0

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
