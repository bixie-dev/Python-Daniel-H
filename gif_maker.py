#!/usr/bin/python3

import glob
import time
import sys
import os

from PIL import Image, ImageDraw, ImageFont

my_color = lambda text, color : "\33[38;5;" + str(color) + "m" + text + "\33[0 m"

# Charaters (3 lines)
# my_lines = [
#     "This is Line Number 1 fkdkfieifislkd",
#     "Line number two and a half eifjs jjjfs aielfls",
#     "and last line 3 "
# ]

my_lines = ["one: This item consins description of",
"two: At specific date yyyy-dd-dd something has happened",
"tree: its been first event ",
"four: 123456789101112131415161718192021222324252627282930313233343536373839404142434445464748",
"five: Scans show that the floors increase in size as you go down",
"Six : fdgdfg dfg fd m k fd rfew cc fdhgfh 4 54 57 5 757 ",
"Seven : kjfll;kdflkjlkjjgfgf fdk f h f sls sls jf gj slg dfg dfhk gsdk gf d df",
"Eight : k gf sjsy djso ot osj dk jf dgk g fdhyj ik fsddf yj r d rewt h e ryh fg g",
"Nine : kljhlkfdh ,d h ;dfsl;l;k gfhgf' ry hgklfg' poijg fhpl'jfgh fghp thppkmht th",
"Ten : kjhgn gfllgh fghofg ghpfpgpkfg hp;kmfhsf hftlkklkm hg fr f fd dert r y t ",
"Eleven : 5n4 54154 5514 111 544 4 4 48 4 14 2351 234 4 4 423 412 2123 1 5 41 nhgjh",
"twelve : fgfgklfgn fghhj gh j gh j;lfkdh;jlfg fgh fd j ghd j dflkjsdh fg jh fdj df ",
"Thirteen : jkjgh fg h fg jf;ldkdf h fg jdfl;fd jhfd j df dg fgh fdj f dfdfdf df d dd",
"fourteen : lkdh gfdfdjkfdlk fgdj dfj df olsd jh dfj d fjh df j df j df j d fj dfjdf ",
"fifteen : kjhg fdjlfh fdjlkdfjh fdj fd dfh dfj fd df j df j df j df j dfh j f d fj",
"Sixteen : kjlhjhkjffkdg lskdjgdsfkl gsdlgjsdlgnlksd gsdflgjsdflkg dsglsjdg lsdg sdfg",
"Seventeen : ;kldf;skg dfsl;gjndshfsfdujh fgh fg jhdf jd f;kjd;flsh fgjh;ldfkjh dfj",
"eighteen : ;kljdfh gfjl'kfjlkfhkfd j jhdkjhkhk h hd h dhh h hhhh hjd h j dhj hj ",
"Ninetheen : lkjhflg dfsh;ljhkhdfs fdojhg;l dfh;lkjh;lgdk h;ljklkjgslk ;hkj;lkgj;l;lkg ",
"Twenty : c<b./,cvbcvb;cb;c gh j gh j hgjghjhgjhgj fgjghjkk popopoiop pp[oi[poipoyur "
]

# Deletes all previous results in [result] folder and [your_awesome.gif] image 
def initialize_result():
    files = glob.glob('result/*')
    for f in files:
        os.remove(f)
    os.remove('your_awesome.gif')
    

# Produces animated gif named [your_awesome.gif] from separate gif images in [result] folder
def make_gif(frame_folder):
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.gif")]
    frame_one = frames[0]
    frame_one.save("your_awesome.gif", format="GIF", append_images=frames, save_all=True, duration=100, loop=0)


number = 1000 # number of beginning of separate gif

# initial position x, y of first letter
xpos = 25
ypos = 25

img = Image.new("RGB", (1500, 600), "white")
draw = ImageDraw.Draw(img)

# Produces every seperate gif
def make_single_gif(character):
    font = ImageFont.truetype("font/Perfect DOS VGA 437.ttf", 25)    
    
    global xpox, ypos, draw
    draw.text((xpos, ypos), character, fill=(0, 255, 0), font=font)
    
    print (my_color((character), 46), end='')
    # sys.stdout.flush()
    # time.sleep(0.001)
    
    global number
    img.save('result/' + str(number) + ".gif")
    number += 1
    
if __name__ == "__main__":
    initialize_result()
    
    for line in my_lines:
        for ch in line:
            make_single_gif(ch)
            xpos += 15
            
        xpos = 25
        ypos += 25
            
    make_gif('result')
            
    