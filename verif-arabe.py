# Controle : chaque chaine arabe affichee doit etre un extrait EXACT de quran.com.
# Rien n'est retape a la main. Ce script NE CORRIGE PLUS tout seul : il constate, et il sort en
# erreur s'il y a un ecart. La correction se fait a la source : on edite le .tpl, on relance
# injecte-arabe.py, on relance ce controle.
import io, re, html, json, subprocess, os, sys

SCR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCR)

def verset(cle):
    out = os.path.join(SCR, ".coran-cache", "verif_%s.json" % cle.replace(":", "_"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    subprocess.run(["curl", "-s", "--ssl-no-revoke", "-A", "Mozilla/5.0",
                    "https://api.quran.com/api/v4/verses/by_key/%s?fields=text_uthmani" % cle,
                    "-o", out], check=True)
    return " ".join(json.load(io.open(out, encoding="utf-8"))["verse"]["text_uthmani"].split())

PAGES = ["tadabbur/index.html"] + ["tadabbur/%03d/index.html" % n for n in range(1, 6)]

# (fichier, classe CSS, cle) — le verset affiche doit etre le verset complet
CIBLES = [
    ("tadabbur/index.html",     "v-ar", "47:24"),
    ("tadabbur/001/index.html", "v-ar", "102:8"),
    ("tadabbur/002/index.html", "v-ar", "10:58"),
    ("tadabbur/003/index.html", "v-ar", "8:11"),
    ("tadabbur/004/index.html", "v-ar", "18:82"),
    ("tadabbur/005/index.html", "v-ar", "2:35"),
]
# les fragments isoles des blocs "Dans la langue" : doivent etre inclus dans leur verset
MOTS = [
    ("tadabbur/003/index.html", "8:11"),
    ("tadabbur/004/index.html", "18:82"),
    ("tadabbur/005/index.html", "2:35"),
]
# les cartes de l'index, dans l'ordre d'apparition
CARTES = ["102:8", "10:58", "8:11", "18:82", "2:35"]

ecarts = []

def dit(libelle, ok, ecrit=None, src=None):
    print("%-46s %s" % (libelle, "OK" if ok else "ECART"))
    if not ok:
        ecarts.append(libelle)
        print("   ecrit  : %s" % ecrit)
        print("   source : %s" % src)

for f, cls, cle in CIBLES:
    s = io.open(f, encoding="utf-8").read()
    m = re.search(r'class="%s"[^>]*>([^<]+)<' % cls, s)
    ecrit = " ".join(html.unescape(m.group(1)).split())
    src = verset(cle)
    dit("%s  %s" % (f, cle), ecrit == src, ecrit, src)

for f, cle in MOTS:
    s = io.open(f, encoding="utf-8").read()
    src = verset(cle)
    frags = re.findall(r'class="l-ar"[^>]*>([^<]+)<', s)
    if not frags:
        dit("  %s  bloc langue" % os.path.dirname(f), False, "(aucun fragment)", cle)
    for i, frag in enumerate(frags):
        e = " ".join(html.unescape(frag).split())
        dit("  %s  fragment %d de %s" % (os.path.dirname(f), i + 1, cle), e in src, e, src)

s = io.open("tadabbur/index.html", encoding="utf-8").read()
cartes = re.findall(r'class="card-ar"[^>]*>([^<]+)<', s)
if len(cartes) != len(CARTES):
    dit("  nombre de cartes", False, len(cartes), len(CARTES))
for extrait, cle in zip(cartes, CARTES):
    e = " ".join(html.unescape(extrait).split())
    src = verset(cle)
    dit("  carte %s" % cle, e in src, e, src)

# Le verset du pied de page (38:29) est repete sur chaque page : il doit venir de la source, lui aussi.
src = verset("38:29")
for f in PAGES:
    s = io.open(f, encoding="utf-8").read()
    m = re.search(r'class="f-ar"[^>]*>([^<]+)<', s)
    e = " ".join(html.unescape(m.group(1)).split()) if m else "(absent)"
    dit("  pied 38:29  %s" % f, m is not None and e in src, e, src)

# Piege d'encodage : une voyelle IMMEDIATEMENT suivie d'une shadda. C'est l'ordre que produit une
# normalisation NFC ; le rasm uthmani de quran.com place la shadda AVANT la voyelle. A l'ecran, la
# difference se voit ; en NFC, la comparaison ne la voit pas. D'ou ce controle a part.
INVERSE = re.compile("[ً-ِْٰ]ّ")
for dp, dns, fs in os.walk("tadabbur"):
    for f in sorted(fs):
        if not f.endswith((".html", ".tpl")):
            continue
        fp = os.path.join(dp, f).replace("\\", "/")
        n = len(INVERSE.findall(io.open(fp, encoding="utf-8").read()))
        if n:
            dit("  encodage  %s" % fp, False, "%d voyelle(s) avant shadda" % n, "shadda avant voyelle")

print("\n%d ecart(s)." % len(ecarts))
sys.exit(1 if ecarts else 0)
