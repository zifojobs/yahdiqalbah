"""Génère sitemap.xml à partir des pages index.html suivies par git (version commitée, pas la copie locale).

À relancer après chaque nouvelle page poussée : python gen_sitemap.py
"""
import subprocess
from pathlib import Path

RACINE = Path(__file__).parent
SITE = "https://yahdiqalbah.com"


def git(*args):
    return subprocess.check_output(["git", "-C", str(RACINE), *args], text=True, encoding="utf-8").strip()


pages = sorted(f for f in git("ls-files").split("\n") if f.endswith("index.html"))
lignes = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for f in pages:
    url = SITE + "/" + f.removesuffix("index.html")
    date = git("log", "-1", "--format=%cs", "HEAD", "--", f)
    lignes.append(f"  <url><loc>{url}</loc><lastmod>{date}</lastmod></url>")
lignes.append("</urlset>")
(RACINE / "sitemap.xml").write_text("\n".join(lignes) + "\n", encoding="utf-8")
print(len(pages), "pages")
