# -*- coding: utf-8 -*-
"""Genere assets/og.png — la carte affichee quand un lien du site est partage.

WhatsApp est le canal reel de diffusion : sans og:image, le lien s'affiche en
petit bloc gris sans visuel. 1200x630 = le ratio 1.91:1 attendu par WhatsApp,
Facebook et LinkedIn.

Le logo est du dore sur fond NOIR PUR, alors que le site est en #0D0B07 : on
reconstruit donc son alpha depuis la luminance, sinon un carre noir apparait.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
NOIR = (13, 11, 7)
OR = (201, 169, 98)
OR_SOMBRE = (138, 112, 56)
CREME = (245, 238, 223)
MUTED = (156, 147, 126)

F = "C:/Windows/Fonts/"
serif = lambda s: ImageFont.truetype(F + "constan.ttf", s)
sans = lambda s: ImageFont.truetype(F + "segoeui.ttf", s)


def centre(d, y, texte, font, fill, tracking=0):
    """Dessine `texte` centre horizontalement. tracking = espacement en px."""
    if tracking:
        largeur = sum(d.textlength(c, font=font) + tracking for c in texte) - tracking
        x = (W - largeur) / 2
        for c in texte:
            d.text((x, y), c, font=font, fill=fill)
            x += d.textlength(c, font=font) + tracking
    else:
        d.text((W / 2, y), texte, font=font, fill=fill, anchor="ma")


img = Image.new("RGB", (W, H), NOIR)

# Halo dore derriere le logo — dessine en basse resolution puis agrandi,
# c'est ce qui donne un degrade lisse sans boucle par pixel.
halo = Image.new("L", (60, 60), 0)
hd = ImageDraw.Draw(halo)
for i in range(30, 0, -1):
    hd.ellipse([30 - i, 30 - i, 30 + i, 30 + i], fill=int(46 * (1 - i / 30) ** 2))
halo = halo.resize((900, 900), Image.LANCZOS)
img.paste(Image.new("RGB", (900, 900), OR), ((W - 900) // 2, -330), halo)

d = ImageDraw.Draw(img)

# Logo : alpha reconstruit depuis la luminance (fond noir -> transparent).
logo = Image.open("assets/logo.png").convert("RGB")
alpha = logo.convert("L").point(lambda v: min(255, int(v * 1.9)))
logo.putalpha(alpha)
logo = logo.resize((150, 150), Image.LANCZOS)
img.paste(logo, ((W - 150) // 2, 62), logo)

centre(d, 238, "INSTITUT YAHDI QALBAH", sans(19), OR, tracking=7)
centre(d, 286, "Enseigner et faire aimer", serif(62), CREME)
centre(d, 358, "le Coran", serif(62), CREME)

d.line([(W / 2 - 90, 462), (W / 2 + 90, 462)], fill=OR_SOMBRE, width=1)

centre(d, 492, "La Chaîne des Prophètes  ·  Les 99 Noms d'Allah  ·  La Seerah",
       sans(26), MUTED)
centre(d, 546, "Gratuit  ·  Sourcé  ·  Sadaqa jariya", sans(20), OR_SOMBRE)

d.rectangle([18, 18, W - 19, H - 19], outline=(40, 33, 18), width=1)

img.save("assets/og.png", optimize=True)
print("assets/og.png", img.size)
