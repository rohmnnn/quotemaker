from PIL import Image, ImageDraw, ImageFont
import textwrap
import requests
import uuid

# text
quotetxt = str(input('Kalimat : '))

# bikin list text, biar raphi
xx = textwrap.wrap(quotetxt, width=40)
print(xx)

# ambil foto dari unplash
# https://source.unsplash.com/640x640/?korea

#background = Image.open('path/img.jpg').convert('RGBA') #internal foto
background = Image.open(requests.get('https://source.unsplash.com/640x640/?japan,korea', stream=True).raw).convert('RGBA') #random photo

# foto overlay
overlaw = Image.open("assets/overlay.png").convert('RGBA')

# gabungin foto + overlaw
fto = Image.blend(overlaw, background, 0.5)

draw = ImageDraw.Draw(fto)
font = ImageFont.truetype('assets/font.ttf', 26)

# atas, paf = atas->bawah, jarak antar baris
atas, paf = 300, 10

# tulis text ke gambar, sesuai list
for i in xx:
    w, h = draw.textsize(i, font=font)
    draw.text(((640 - w) / 2, atas), i, font=font)
    atas += h + paf

# show fix image
#fto.show()

# save
rndn = str(uuid.uuid4())
fto.save('save/'+rndn+'.PNG')
print('disini sayang: save/'+rndn+'.PNG')






