# Injecte l'arabe dans les gabarits a jetons, depuis quran.com UNIQUEMENT.
# Regle du parc : l'arabe ne se retape jamais a la main.
#
#   @@AR:s:v@@         -> le verset complet (rasm uthmani)
#   @@S:s:v:a:b@@      -> les mots [a, b[ du verset
#   @@W:s:v:i@@        -> le mot i du verset
#   @@CH:s@@           -> le nom arabe de la sourate
#
# Les .tpl sont la source ; les index.html sont generes. On ne modifie jamais un index.html a la main.
import io, os, re, json, subprocess, sys

SCR = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(SCR, ".coran-cache")
os.makedirs(CACHE, exist_ok=True)

def _get(url, nom):
    out = os.path.join(CACHE, nom + ".json")
    if not os.path.exists(out):
        subprocess.run(["curl", "-s", "--ssl-no-revoke", "-A", "Mozilla/5.0", url, "-o", out], check=True)
    return json.load(io.open(out, encoding="utf-8"))

def verset(cle):
    d = _get("https://api.quran.com/api/v4/verses/by_key/%s?fields=text_uthmani" % cle,
             "v_" + cle.replace(":", "_"))
    return d["verse"]["text_uthmani"]

def sourate(num):
    d = _get("https://api.quran.com/api/v4/chapters/%s" % num, "c_" + str(num))
    return d["chapter"]["name_arabic"]

def resous(m):
    p = m.group(1).split(":")
    if p[0] == "CH":
        return sourate(p[1])
    cle = "%s:%s" % (p[1], p[2])
    mots = verset(cle).split()
    if p[0] == "AR":
        return " ".join(mots)
    if p[0] == "W":
        return mots[int(p[3])]
    if p[0] == "S":
        return " ".join(mots[int(p[3]):int(p[4])])
    raise ValueError(m.group(0))

JETON = re.compile(r"@@([A-Z]+(?::[0-9]+)+)@@")

cibles = sys.argv[1:] or [os.path.join(dp, f)
                          for dp, _, fs in os.walk(SCR) for f in fs if f.endswith(".tpl")]
for tpl in cibles:
    src = io.open(tpl, encoding="utf-8").read()
    n = len(JETON.findall(src))
    dst = tpl[:-4] if tpl.endswith(".tpl") else tpl + ".html"
    io.open(dst, "w", encoding="utf-8").write(JETON.sub(resous, src))
    print("%-58s %2d jetons -> %s" % (os.path.relpath(tpl, SCR), n, os.path.relpath(dst, SCR)))
