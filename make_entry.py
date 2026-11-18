from PIL import Image, ImageDraw, ImageFont
import os

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
W = H = 1024
img = Image.new("RGB", (W, H), (16, 18, 24))
d = ImageDraw.Draw(img)

def f(size, bold=True):
    return ImageFont.truetype(FONT if bold else FONT_R, size)

def text(x, y, s, size, color=(240,240,240), bold=True, anchor="la"):
    d.text((x, y), s, font=f(size, bold), fill=color, anchor=anchor)

d.rectangle([0,0,W,112], fill=(196,42,42))
text(26, 12, "17 NOV 2026", 56, (255,255,255))
text(998, 22, "MONDE", 21, (255,225,225), anchor="ra")

stories = [
    ("IRAN", "Drones contre une base US", "Bahreïn ; riposte sur la mer", (232,118,74)),
    ("UKRAINE", "Frappes croisées sur les ponts", "Crimée et ponts ukrainiens", (78,158,230)),
    ("MONGOLIE", "Le président démissionne", "fonds ferroviaires contestés", (110,198,150)),
    ("JAPON", "Avions russes sur le Japon", "Tokyo proteste, chasseurs au décollage", (232,200,78)),
    ("ALLEMAGNE", "Deutsche Bank : 15 M de documents", "l'action chute d'environ 6 %", (168,148,230)),
    ("ÉTATS-UNIS", "La rougeole n'est plus 'éliminée'", "5 400 cas, vaccinations en baisse", (232,92,108)),
]

x0, y0 = 26, 138
cw, ch, gap = 478, 236, 16
for i, (tag, t1, t2, acc) in enumerate(stories):
    r, c = divmod(i, 2)
    x = x0 + c*(cw+gap); y = y0 + r*(ch+gap)
    d.rounded_rectangle([x,y,x+cw,y+ch], radius=16, fill=(32,36,46), outline=acc, width=4)
    tw = d.textlength(tag, font=f(16)) + 24
    d.rounded_rectangle([x+16,y+16,x+16+tw,y+44], radius=8, fill=acc)
    text(x+28, y+20, tag, 16, (20,20,20))   # left anchor, no vertical centering tricks
    text(x+16, y+58, t1, 27, (245,245,245))
    text(x+16, y+98, t2, 20, (175,180,190), bold=False)
    for k in range(3):
        d.ellipse([x+16+k*20, y+ch-36, x+27+k*20, y+ch-25], fill=acc)

d.rectangle([0, H-42, W, H], fill=(10,11,16))
text(26, H-22, "Les unes du jour — d'après les dépêches du 17 novembre 2026", 16, (140,145,155), bold=False)
text(998, H-22, "make.fun", 16, (140,145,155), anchor="ra", bold=False)

img.save("entry.png", optimize=True)
print("entry.png", os.path.getsize("entry.png"), "bytes")
