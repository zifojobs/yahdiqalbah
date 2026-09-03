import io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _assemble import page

ICI = os.path.dirname(os.path.abspath(__file__))
corps = lambda n: io.open(os.path.join(ICI, "%s.corps.html" % n), encoding="utf-8").read()

page("004",
     titre="Une lettre qui attend que tu grandisses — Sourate Al-Kahf 18 : 82 — Tadabbur",
     desc="Le mur d'Al-Kahf ne tenait pas : il attendait. Et le trésor change de nom entre le début et la fin du verset — une seule lettre sépare « pour eux » de « le leur ».",
     og_desc="Le mur ne tenait pas. Il attendait.",
     sourate="@@CH:18@@",
     h1="Une lettre qui attend que tu grandisses",
     ref="Sourate Al-Kahf, 18 : 82",
     kicker="Tadabbur · Verset 4",
     corps=corps("004"), prev="003", nxt="005")

page("005",
     titre="Habite — Sourate Al-Baqarah 2 : 35 — Tadabbur",
     desc="Le premier ordre donné au premier homme n'est pas un ordre de faire, c'est un ordre d'habiter. Et le mot employé porte la même racine que la tranquillité.",
     og_desc="Le premier ordre donné à l'homme n'est pas de faire. C'est d'habiter.",
     sourate="@@CH:2@@",
     h1="Habite",
     ref="Sourate Al-Baqarah, 2 : 35",
     kicker="Tadabbur · Verset 5",
     corps=corps("005"), prev="004", nxt=None)
