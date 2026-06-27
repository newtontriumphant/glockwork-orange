Made by: @zsharpminor // gh/newtontriumphant // udo funke

Repository link: https://github.com/newtontriumphant/glockwork-orange/

Total hours so far: 15.0

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

## [06/24/26 | 4.0 hours]

### The PCB Schematic!

I've procrastinated this for wayy too long. After doing some intense research, I figured out it would be best if I used a 15V power supply and had 10 PCBs which each fed to 3 solenoids, for a total of 30 solenoids. For a 15V schematic, I need a boatload of 2N3904 transistors, though. Let's get to it!

![schem1](https://cdn.hackclub.com/019efcd0-ae68-7e45-a850-c60c058c2212/Screenshot%202026-06-24%20at%208.26.33%E2%80%AFPM.png)

I have a plan. It may not seem like it now, but I do. I promise :3

I then proceeded to spend an ENTIRE HOUR researching MOSFETs. No, I'm not joking. The original MOSFET I had thought of for this project was unfortunately discontinued and therefore way too expensive, but I found a pretty good drop-in replacement: the IRF530NPBF and IRLZ44NBPF would both be good options - the 530 would require a step-up, though, so I ultimately went with the IRLZ44N.

I also subtly stole the idea of having a hardware-coded flashing LED from [this project](https://engineering.tamu.edu/news/2019/05/the-autospiel-computer-engineering-students-merge-disciplines-to-automate-music.html). With that, the first draft of the schematic was done:

![schem2](https://cdn.hackclub.com/019effef-3dd9-7076-8a8c-d5d738aad5e2/Screenshot%202026-06-25%20at%2010.58.47%E2%80%AFAM.png)

After running ERC and getting only the usual power pin not driven by output pin lines, I thought I was in the clear, until I double-checked the datasheets and realized I FORGOT the MOST IMPORTANT PART: the 15v net! Also, the capacitors. Caps will always be the death of me, but after some research (and quite a bit of asking Claude), I realized my mistake, and fixed the schematic fully:

![schem3](https://cdn.hackclub.com/019efff7-91c2-75e1-8acf-26b3bc5a9644/Screenshot%202026-06-25%20at%2011.07.52%E2%80%AFAM.png)

After some quick copy-pasting, and the addition of mounting holes and screw terminals to infinitely combine multiple PCBs, I ended up with this (I also realized what PWR_FLAG is actually used for...):

![schemfinal](https://cdn.hackclub.com/019f0001-06cc-740c-9fb7-c1abf7168b04/Screenshot%202026-06-25%20at%2011.18.10%E2%80%AFAM.png)

### Assigning Footprints

I don't know why, but this is always my least favorite part of making a PCB. I usually have to do this like six or seven times over before I get it right, and this wasn't much of an exception: after forty minutes, I finally had a good assignment that I was happy with. Thankfully, I was able to copy and paste most of the footprints. This is also where I locked in M2 as my choice for screws!

![footprints](https://cdn.hackclub.com/019f003e-79e4-7bee-828e-a1ed926fd007/Screenshot%202026-06-25%20at%2012.25.18%E2%80%AFPM.png)

(Yes, I had to make a custom footprint. I hate my wife.)

![pcb1](https://cdn.hackclub.com/019f0040-53d1-720b-b674-f744cd66119c/Screenshot%202026-06-25%20at%2012.27.17%E2%80%AFPM.png)

Hey, that looks pretty decent. I'll get onto the PCB routing tomorrow! :D

## [06/25/26 | 4.0 hours]

### Routing...

I don't even want to describe the pain I'm going through. PCB routing will be the death of me.

![p1](https://cdn.hackclub.com/019f007c-2f45-72e6-aa11-b71edfb1f492/Screenshot%202026-06-25%20at%201.32.41%E2%80%AFPM.png)

yes, I know this layout probably won't work. let my stupid brain at least prove it to myself

![p2](https://cdn.hackclub.com/019f0086-ae13-771b-b573-389c931c8024/Screenshot%202026-06-25%20at%201.44.09%E2%80%AFPM.png)

hold up... maybe it will work after all! lemme fix up my drc and get my silkscreen non-conflicting:

![drc](https://cdn.hackclub.com/019f009b-5e57-7038-aaed-e8b5e43c966c/Screenshot%202026-06-25%20at%202.06.47%E2%80%AFPM.png)

Okay, here's the final routing for now. I'm getting some other people to sanity check it, but for now, four hours later, the PCB is routed! :D

![fpcb](https://cdn.hackclub.com/019f00a0-8d96-7c28-8839-a5dfb8590c4f/Screenshot%202026-06-25%20at%202.12.25%E2%80%AFPM.png)

![pcb3d](https://cdn.hackclub.com/019f00a2-ba3f-70bc-9930-d3b393344285/Screenshot%202026-06-25%20at%202.14.49%E2%80%AFPM.png)

Tomorrow, I can finally get all of this into CAD. :D

## [06/26/26 | 2.0 hours]

### Modeling the PCB Holders

![pcbmodel](https://cdn.hackclub.com/019f0713-5e10-76ee-ac63-0468bde2a9dd/Screenshot%202026-06-26%20at%208.15.23%E2%80%AFPM.png)

I began by exporting the PCB as a .STEP file and importing it into Fusion. I then took some measurements and began my work on the PCB holder (see above.) The PCB is going to be mounted to this holder with 4 M2 screws, and a crap ton of M2 screws will be used in this assembly. Since my PCB had some signal wires on the bottom, as well as some hefty MOSFET leads, I had to make some additional cutouts:

![cutoutone](https://cdn.hackclub.com/019f0718-ec12-72bc-a1cc-b2626b7cf78c/Screenshot%202026-06-26%20at%208.21.38%E2%80%AFPM.png)

![cutouttwo](https://cdn.hackclub.com/019f071b-3c83-7636-9cf1-1cf4454d677f/Screenshot%202026-06-26%20at%208.24.09%E2%80%AFPM.png)

Then, the PCB holder was done! I settled for an interlocking design so that I could keep rowing these together! :D

![interlocking](https://cdn.hackclub.com/019f071f-0c32-7bab-8173-c3651432c9cf/Screenshot%202026-06-26%20at%208.28.16%E2%80%AFPM.png)

The final PCB holder was as follows:

![pcbholderfinal1](https://cdn.hackclub.com/019f0722-7bd3-7151-8da4-59985f765a7c/Screenshot%202026-06-26%20at%208.32.03%E2%80%AFPM.png)

![pcbholderfinal2](https://cdn.hackclub.com/019f0722-a4ba-7e0b-897a-2681e045cd07/Screenshot%202026-06-26%20at%208.32.16%E2%80%AFPM.png)

With that done, I was finally able to get over to the master assembly!

### Assembly, Part One

After about 30 minutes, I was able to get all the PCBs in place. My plan is to screw all of this into a plywood surface, maybe an old desk or a plywood panel, something like this:

![plywoodpanel](https://i5.walmartimages.com/asr/3a0db82c-44aa-40fd-a24b-f473ea6acc01.84121b1dbe6053e71265afc7d6bfde7c.jpeg)

Anyways, I need to find a model for that in Fusion. Before we get there, here's what I got so far:

![assembled1](https://cdn.hackclub.com/019f0734-bf0f-7505-9431-86d4befae2db/Screenshot%202026-06-26%20at%208.51.58%E2%80%AFPM.png)

The plan here is to power everything with an Arduino Mega 2560 and have the cables routed underneath the PCBs, where there's some wiggle room in between the screw mounts and the plywood. The whole project is definitely coming back together now! Let me find that checklist that I put together a few days ago...

- [x] Find a working solenoid
- [x] Find a working glockenspiel
- [x] 3D model the solenoid holder
- [x] Schematic for PCB
- [x] Routing for PCB
- [ ] 3D model the glock holder
- [ ] Find a way to power the solenoids
- [ ] Write a compelling README
- [ ] ship :3

Well, hey, we're almost there! I also know just what I'll use for the power - I'm taking inspiration from a similar self-playing project that uses a [Meanwell AC/DC converter](https://www.digikey.com/en/products/detail/mean-well-usa-inc/LRS-200-15/7705023) as opposed to a bench power supply, and I think that it would look dope on a plywood panel, so I'm going for that. First thing tomorrow, I'm going to incorporate this into my design! Until next time! :D 