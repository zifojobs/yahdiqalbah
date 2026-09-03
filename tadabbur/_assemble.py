# Assemble un verset Tadabbur : la coquille (tete + pied) est celle de 003, le corps est propre a chaque verset.
# Sortie = un .tpl a jetons, que injecte-arabe.py transforme en index.html avec l'arabe de quran.com.
import io, os, re

ICI = os.path.dirname(os.path.abspath(__file__))
BASE = io.open(os.path.join(ICI, "003", "index.html.tpl"), encoding="utf-8").read()

TETE = BASE.split("<article>")[0]
PIED = "<nav class=\"serie-nav\"" + BASE.split("<nav class=\"serie-nav\"", 1)[1]

def page(num, titre, desc, og_desc, sourate, h1, ref, kicker, corps, prev, nxt):
    t = TETE
    t = re.sub(r"<title>.*?</title>", "<title>%s</title>" % titre, t, flags=re.S)
    t = re.sub(r'(<meta name="description" content=)".*?"', lambda m: m.group(1) + '"%s"' % desc, t, flags=re.S)
    t = re.sub(r'(<meta property="og:title" content=)".*?"', lambda m: m.group(1) + '"%s"' % titre.split(" — Tadabbur")[0], t, flags=re.S)
    t = re.sub(r'(<meta property="og:description" content=)".*?"', lambda m: m.group(1) + '"%s"' % og_desc, t, flags=re.S)
    t = t.replace("/tadabbur/003/", "/tadabbur/%s/" % num)
    t = t.replace("Tadabbur · Verset 3", kicker)
    t = t.replace("@@CH:8@@", sourate)
    t = re.sub(r"<h1>.*?</h1>", "<h1>%s</h1>" % h1, t, flags=re.S)
    t = re.sub(r'<span class="ep-badge">.*?</span>', '<span class="ep-badge">%s</span>' % ref, t, flags=re.S)

    p = PIED
    p = re.sub(r'<a href="/tadabbur/002/">← Verset précédent</a>',
               '<a href="/tadabbur/%s/">← Verset précédent</a>' % prev, p)
    if nxt:
        p = p.replace('<a href="/tadabbur/004/">Verset suivant →</a>',
                      '<a href="/tadabbur/%s/">Verset suivant →</a>' % nxt)
    else:
        p = p.replace('  <a href="/tadabbur/004/">Verset suivant →</a>\n', "")

    dst = os.path.join(ICI, num, "index.html.tpl")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    io.open(dst, "w", encoding="utf-8").write(t + "<article>\n" + corps + "\n</article>\n\n" + p)
    print("ecrit %s" % os.path.relpath(dst, ICI))
