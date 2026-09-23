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
     corps=corps("005"), prev="004", nxt="006")

page("006",
     titre="Le désir et la chute portent le même mot — Sourate Al-Jâthiyah 45 : 23 — Tadabbur",
     desc="Le verset ne parle pas de l'intensité d'une passion, il parle de sa place. Et le mot arabe pour le désir est bâti sur la racine qui dit tomber.",
     og_desc="Le verset ne parle pas de la passion. Il parle de la place.",
     sourate="@@CH:45@@",
     h1="Le désir et la chute portent le même mot",
     ref="Sourate Al-Jâthiyah, 45 : 23",
     kicker="Tadabbur · Verset 6",
     corps=corps("006"), prev="005", nxt="007")

page("007",
     titre="Des années pour comprendre un verset — Sourate Al-Baqarah 2 : 216 — Tadabbur",
     desc="On aime de toutes ses forces ce qui n'est pas à sa place, on laisse à contrecœur ce qui allait devenir un bien. Certains versets se lisent en une minute, et se comprennent en dix ans.",
     og_desc="Certains versets se lisent en une minute, et se comprennent en dix ans.",
     sourate="@@CH:2@@",
     h1="Des années pour comprendre un verset",
     ref="Sourate Al-Baqarah, 2 : 216",
     kicker="Tadabbur · Verset 7",
     corps=corps("007"), prev="006", nxt="008")

page("008",
     titre="Le souffle qu'on ne programme pas — Sourate Al-Isrâ' 17 : 85 — Tadabbur",
     desc="Un personnage pleure à l'écran, une machine répond avec chaleur. Les signes de l'émotion s'imitent ; le verset ne décrit pas l'âme, il dit de quoi elle relève — et combien peu nous en savons.",
     og_desc="On imite les larmes. On ne programme pas le souffle.",
     sourate="@@CH:17@@",
     h1="Le souffle qu'on ne programme pas",
     ref="Sourate Al-Isrâ', 17 : 85",
     kicker="Tadabbur · Verset 8",
     corps=corps("008"), prev="007", nxt=None)
