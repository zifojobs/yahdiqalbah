# Refonte Yahdi Qalbah — plan d'implémentation

> **Pour les agents :** ce plan s'exécute tâche par tâche. Les étapes sont en cases à cocher
> (`- [ ]`). Spec de référence :
> `docs/superpowers/specs/2026-08-08-refonte-yahdi-qalbah-design.md` — **le lire avant de commencer.**

## État d'avancement — 08/08/2026, 23 h 20

| Task | État | Commit |
|---|---|---|
| 1 — coquille partagée | ✅ **en production, vérifiée en direct** | `98d22ad` |
| 2 — accueil sombre + volumes | ✅ **en production, vérifiée en direct** | `9416053` |
| 3 — gabarit de lecture clair | ✅ **en production, validée par Saïbo** | `a066e5d` + `9983050` |
| 4 — une page par épisode Seerah | ✅ **en production, vérifiée en direct** | `f6371d7` |
| 5 — page de participation | ⏸️ bloquée : libellé validé + vrais numéros | — |

**Comment la Task 3 a été menée** — d'abord sur **un seul écran** (`seerah/001/`, `a066e5d`),
validé par Saïbo, *puis* propagée (`9983050`). C'est la règle du 01/08 : un registre visuel se
tranche sur une page, pas après seize heures de propagation.

Deux traitements distincts, et c'est voulu :
- `seerah/001/` reçoit le **gabarit complet** `.lecture` (feuille crème, mesure 65ch, serif,
  bloc `.sources` visible). C'est le gabarit que reproduiront les épisodes 002 à 005.
- `noms/` et `prophetes/` reçoivent **la palette seulement**, en bloc ajouté à la fin de leur
  `<style>` (à spécificité égale, le dernier gagne). Leur typographie et leur structure propres
  sont conservées : ce sont des lecteurs modaux, pas des articles. **47 lignes ajoutées, zéro
  supprimée** — les règles sombres sont recouvertes, donc réversibles en un commit.
- Le **voile du modal reste sombre** dans les deux cas : seule la feuille passe au crème.

🔴 **Deux corrections apportées au plan par le code réel :**

1. **`noms/` et `prophetes/` ne servent aucun contenu en HTML.** `<div class="grid" id="grid">`
   est vide ; les 52 notices et les 25 récits vivent dans des tableaux JavaScript
   (`const NOMS = […]`, `const PROPHETES=[…]`) injectés à l'exécution et lus dans un modal
   `#reader`. ⇒ **le critère V4 (« les 3 pages restent lisibles avec JS désactivé ») est
   infaisable en Task 3** — et l'était déjà avant la refonte. Il est reformulé en « la page
   reste **navigable** sans JS » (vrai, livré en Task 1). « Contenu servi sans JS » relève du
   chantier de **découpage des 99 Noms**, déjà prévu après cette refonte.
2. **La Task 3 n'est pas un conteneur à ajouter, c'est repeindre trois lecteurs.** Chacun porte
   20 à 30 règles de couleur sombres en dur (`.sheet h3`, `.panel .p-ar`, `article p{color:#dcd3bd}`…).
   Les cibles correctes de `.lecture` sont `#sheet` (noms), `#pbody` (prophetes) et l'`<article>`
   de `seerah/001/`. ⚠️ **Piège de cascade** : `site.css` est chargé **avant** le `<style>` de
   chaque page ⇒ à égalité de spécificité, la page gagne. Prévoir des sélecteurs composés
   (`#sheet.lecture`) ou déplacer le lien après le `<style>`.

**Écarts assumés par rapport au plan écrit :**
- Les cartes de l'accueil gardent la classe `.card` existante (le JS de révélation en dépend) ;
  `.espace-volume` y est simplement ajouté. Les 5 cartes sont conservées — supprimer celle du
  cours d'arabe aurait retiré la seule couche qui rapporte.
- Le lien flottant « ← Accueil » des 3 sous-pages a été retiré (markup + CSS) : en
  `position:fixed;top:1rem;left:1rem`, il recouvrait le logo du nouvel en-tête.
- Le pied de page propre à chaque page est **conservé** (il porte du contenu spécifique) ;
  le pied institutionnel s'ajoute après.

🔶 **Signalé, pas corrigé** — le pied de `seerah/index.html` porte le verset **7:180**
(« les plus beaux noms »), qui est celui des 99 Noms. Contenu religieux : arbitrage de Saïbo.

---

**But :** donner au site une allure institutionnelle — navigation permanente, cohérence entre
les 4 pages, lecture confortable sur les textes longs, et une page de participation.

**Architecture :** feuille de style partagée (`assets/site.css`) + markup d'en-tête et de pied
répété dans chaque page. Aucune étape de construction, aucune dépendance. La navigation est du
HTML pur : elle fonctionne JavaScript désactivé.

**Stack :** HTML / CSS / JS vanilla. Déploiement Vercel par `git push origin main`.

## Contraintes globales

Ces règles s'appliquent à **toutes** les tâches, sans rappel :

- **Aucune dépendance externe ajoutée.** Ni police distante, ni CDN, ni bibliothèque.
- **La navigation fonctionne sans JavaScript.** Le JS est réservé au confort (reprise de
  lecture, bouton copier) et sa panne ne doit jamais rendre une page inutilisable.
- **Aucune page ne dépasse 150 Ko.**
- **Jamais le Nom d'Allah en décor**, filigrane ou texture de fond. S'il apparaît, il domine la page.
- **Décor strictement non figuratif** : géométrie islamique en SVG, aucun être vivant, jamais le
  Prophète ﷺ ni les compagnons. **Le ghayb ne s'illustre pas.**
- **Aucune image générée par IA.** Construction en code pur.
- Registre **contemplatif d'adulte** : aucune mascotte, rien de ludique.
- Interface et contenu **en français**.
- **Le rendu visuel se juge par Saïbo dans son navigateur.** Aucune capture, aucun Playwright.
- **Vérification en direct après déploiement**, sur `yahdiqalbah.com`, jamais sur le fichier local.

## Note sur les vérifications

Le projet n'a pas de lanceur de tests, et ne doit pas en acquérir. Chaque tâche se termine
donc par deux contrôles :

1. **Mécanique** — une commande shell qui échoue ou réussit sans ambiguïté.
2. **Visuel** — confié à Saïbo, explicitement formulé (« ouvre telle page, tu dois voir ceci »).

Ne jamais cocher une étape sur une impression. Si la commande n'a pas été lancée, l'étape n'est
pas faite.

## Structure des fichiers

| Fichier | Responsabilité |
|---|---|
| `assets/site.css` | **Créé.** Jetons de couleur et de typo, en-tête, navigation, pied, boutons, gabarit de lecture clair. Seule source de la cohérence entre pages. |
| `index.html` | Modifié. Accueil sombre : hero, espaces avec volumes, engagements, participation. |
| `noms/index.html` | Modifié. Reçoit la coquille + le gabarit de lecture clair. Contenu inchangé. |
| `prophetes/index.html` | Modifié. Idem. |
| `seerah/index.html` | Modifié → devient **l'index** de la série (sombre, sélection). |
| `seerah/001/index.html` | **Créé.** L'épisode 1 migré, cas de référence du gabarit d'épisode. |
| `participer/index.html` | **Créé.** Page de participation. |

---

## Task 1 : la coquille partagée

**Fichiers**
- Créer : `assets/site.css`
- Modifier : `index.html`, `noms/index.html`, `prophetes/index.html`, `seerah/index.html`

**Interfaces**
- *Produit* — les jetons CSS que toutes les tâches suivantes consomment :
  `--encre` (fond sombre), `--creme` (fond clair de lecture), `--or` (accent),
  `--sans`, `--serif`, `--ar` (les 3 familles, **reprendre les valeurs déjà définies dans
  `index.html`**, ne pas en inventer).
- *Produit* — les classes `.site-header`, `.site-nav`, `.site-footer`, `.btn-or`.

- [ ] **Étape 1 : relever les valeurs typographiques existantes**

```bash
cd "E:/YAHDI QALBAH/prophetes-timeline"
grep -oE "\-\-(ar|sans|serif|or|encre)[^;]*;" index.html | sort -u
```

Reporter ces valeurs telles quelles dans `assets/site.css`. **Ne pas changer les polices** :
ce n'est pas dans le périmètre, et elles sont déjà cohérentes entre les 4 pages.

- [ ] **Étape 2 : créer `assets/site.css`**

Il contient, dans cet ordre : les jetons `:root`, la remise à zéro minimale, `.site-header`,
`.site-nav`, `.site-footer`, `.btn-or`. **Rien d'autre pour l'instant** — le gabarit de lecture
arrive en Task 3.

- [ ] **Étape 3 : écrire le markup de la coquille**

Ce bloc est le **contrat partagé**. Il se répète à l'identique dans les 4 pages ; seul
`aria-current="page"` se déplace sur le lien de la page courante. Les chemins sont **absolus**
(`/…`) pour rester justes quelle que soit la profondeur.

```html
<header class="site-header">
  <a class="site-brand" href="/">
    <img src="/assets/logo.png" alt="" width="36" height="36">
    <span>Yahdi Qalbah</span>
  </a>
  <nav class="site-nav" aria-label="Espaces">
    <a href="/prophetes/">Les Prophètes</a>
    <a href="/noms/">Les 99 Noms</a>
    <a href="/seerah/">La Seerah</a>
    <a href="/participer/" class="btn-or">Participer</a>
  </nav>
</header>
```

⚠️ `alt=""` sur le logo est **voulu** : le nom de l'institut est déjà dans le texte juste à côté ;
le répéter ferait bégayer un lecteur d'écran.

⚠️ `/participer/` n'existera qu'en Task 5. Le lien mènera à un 404 d'ici là — c'est accepté et
c'est la raison pour laquelle Task 5 ne doit pas être sautée.

- [ ] **Étape 4 : poser la coquille dans les 4 pages**

Dans chaque fichier : ajouter `<link rel="stylesheet" href="/assets/site.css">` dans le `<head>`,
insérer le `<header>` juste après `<body>`, et le pied de page avant `</body>`. **Ne rien
supprimer du contenu existant.**

- [ ] **Étape 5 : vérification mécanique**

```bash
cd "E:/YAHDI QALBAH/prophetes-timeline"
# V1a — les 4 pages ont une navigation
for f in index.html noms/index.html prophetes/index.html seerah/index.html; do
  printf "%-24s nav=%s css=%s\n" "$f" \
    "$(grep -c '<nav class="site-nav"' $f)" \
    "$(grep -c 'assets/site.css' $f)"
done
# attendu : nav=1 et css=1 sur les 4 lignes

# V7 — aucune page au-dessus de 150 Ko
find . -name "*.html" -not -path "./docs/*" -size +150k

# attendu : aucune sortie

# contrainte globale — aucune dépendance externe introduite
grep -lE "https?://(fonts|cdn|unpkg|cdnjs)" assets/site.css
# attendu : aucune sortie
```

- [ ] **Étape 6 : commit**

```bash
git add assets/site.css index.html noms/index.html prophetes/index.html seerah/index.html
git commit -m "Coquille partagee : en-tete, navigation et pied sur les 4 pages"
git push origin main
```

- [ ] **Étape 7 : vérification par Saïbo (V1)**

> Sur `yahdiqalbah.com`, **désactive JavaScript** dans ton navigateur, puis vérifie que depuis
> n'importe laquelle des 4 pages tu atteins les 3 autres en un clic. C'est le critère V1, et
> c'est celui qui protège ton public en réseau faible.

---

## Task 2 : l'accueil sombre

**Fichiers**
- Modifier : `index.html`, `assets/site.css`

**Interfaces**
- *Consomme* : les jetons et classes de la Task 1.
- *Produit* : les classes `.espace-card` et `.espace-volume`, réutilisées nulle part ailleurs
  (elles restent propres à l'accueil).

- [ ] **Étape 1 : relever les volumes réels**

Ne jamais écrire ces nombres de mémoire — les compter dans les fichiers :

```bash
cd "E:/YAHDI QALBAH/prophetes-timeline"
echo "récits prophètes : $(grep -c 'class="recit' prophetes/index.html)"
echo "notices Noms     : $(grep -c 'class="nom' noms/index.html)"
```

Si le sélecteur ne correspond pas au markup réel, l'ajuster puis recompter. **Le nombre affiché
sur l'accueil doit être celui qui est réellement en ligne** (critère V2).

- [ ] **Étape 2 : réécrire la section des espaces**

Trois cartes, chacune portant son volume :

```html
<a class="espace-card" href="/prophetes/">
  <h3>La Chaîne des Prophètes</h3>
  <p class="espace-volume">25 récits sourcés</p>
</a>
<a class="espace-card" href="/noms/">
  <h3>Les 99 Noms d'Allah</h3>
  <p class="espace-volume">52 notices publiées</p>
</a>
<a class="espace-card" href="/seerah/">
  <h3>La Vie du Prophète ﷺ</h3>
  <p class="espace-volume">la série, épisode par épisode</p>
</a>
```

Remplacer `25` et `52` par les nombres comptés à l'étape 1.

- [ ] **Étape 3 : discipliner le hero**

L'univers céleste **reste** — Saïbo l'a validé. Augmenter l'espace noir autour, réduire
l'intensité des effets pour qu'il serve le texte. **Ne pas le remplacer**, ne pas ajouter de
calligraphie en fond.

- [ ] **Étape 4 : ordonner la page**

hero → espaces → **les trois engagements** (sourcé · gratuit · passeur) → bloc participation
sobre → pied. **La participation vient après les engagements, jamais avant.**

- [ ] **Étape 5 : vérification mécanique**

```bash
cd "E:/YAHDI QALBAH/prophetes-timeline"
grep -o 'class="espace-volume">[^<]*' index.html
# attendu : 3 lignes, avec les nombres comptés à l'étape 1

find . -name "index.html" -maxdepth 1 -size +150k   # attendu : aucune sortie
```

- [ ] **Étape 6 : commit**

```bash
git add index.html assets/site.css
git commit -m "Accueil : volumes du fonds affiches sur les cartes, hero discipline"
git push origin main
```

- [ ] **Étape 7 : vérification par Saïbo (V2)**

> Ouvre `yahdiqalbah.com` sur ton téléphone. Les trois volumes affichés correspondent-ils à ce
> qui est réellement en ligne ? Et l'univers céleste te plaît-il toujours une fois calmé ?

---

## Task 3 : le gabarit de lecture clair

**Fichiers**
- Modifier : `assets/site.css`, `noms/index.html`, `prophetes/index.html`, `seerah/index.html`

**Interfaces**
- *Consomme* : les jetons de la Task 1.
- *Produit* : la classe `.lecture` (conteneur de texte long) et `.lecture-ar` (versets et
  hadiths en arabe), consommées par les Tasks 4 et 5.

- [ ] **Étape 1 : ajouter le gabarit à `assets/site.css`**

```css
.lecture {
  background: var(--creme);
  color: var(--encre);
  font-family: var(--serif);
  font-size: 1.06rem;
  line-height: 1.75;
  max-width: 65ch;   /* la mesure qui décide qu'on finit un texte de 70 000 signes */
  margin-inline: auto;
  padding-inline: 1.25rem;
}
.lecture-ar {
  font-family: var(--ar);
  direction: rtl;
  font-size: 1.35em;
  line-height: 2.1;
  margin-block: 1.5em;
}
```

`--creme` est un **crème chaud, jamais `#fff`** : moins d'éblouissement, et l'or y survit
comme accent.

- [ ] **Étape 2 : appliquer aux trois espaces**

Envelopper le corps de texte de chaque page dans `.lecture`. **Le contenu ne change pas** : ni
les 25 récits, ni les 52 notices, ni le texte de l'épisode 1 ne sont réécrits.

Les zones de **sélection** (grille des Noms, frise des Prophètes) restent sombres : le clair est
réservé au texte qu'on lit longuement.

- [ ] **Étape 3 : rendre les sources visibles**

Le contenu du site est intégralement sourcé, et presque aucun site islamique francophone ne le
montre. **C'est le meilleur signal d'institution disponible — il ne doit pas rester discret.**

Ajouter à `assets/site.css` :

```css
.sources {
  font-family: var(--sans);
  font-size: .86rem;
  border-top: 1px solid color-mix(in srgb, var(--encre) 18%, transparent);
  margin-block-start: 2.5rem;
  padding-block-start: 1rem;
}
.sources h3 {
  font-size: .78rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  margin-block-end: .5rem;
}
```

Puis, dans chaque espace, envelopper les mentions de sources déjà présentes dans
`<section class="sources"><h3>Sources</h3>…</section>`. **Ne pas inventer de source** : reprendre
uniquement celles déjà écrites dans le contenu.

- [ ] **Étape 4 : vérification mécanique**

```bash
cd "E:/YAHDI QALBAH/prophetes-timeline"
grep -c "max-width: *65ch" assets/site.css          # attendu : 1
for f in noms prophetes seerah; do
  printf "%-12s lecture=%s\n" "$f" "$(grep -c 'class="lecture' $f/index.html)"
done
# attendu : au moins 1 sur chacun

find . -name "*.html" -not -path "./docs/*" -size +150k   # attendu : aucune sortie
```

```bash
cd "E:/YAHDI QALBAH/prophetes-timeline"
grep -c 'class="sources"' noms/index.html prophetes/index.html seerah/index.html
# attendu : au moins 1 par fichier
```

- [ ] **Étape 5 : commit**

```bash
git add assets/site.css noms/index.html prophetes/index.html seerah/index.html
git commit -m "Gabarit de lecture clair : mesure bornee, arabe et sources traites a part"
git push origin main
```

- [ ] **Étape 6 : vérification par Saïbo (V3 et V4)**

> Sur ton téléphone, ouvre une notice des 99 Noms et un récit de prophète. **Les lignes
> doivent tenir sans que l'œil ait à balayer**, et le fond doit être crème, pas blanc. Puis
> **désactive JavaScript** : les trois pages doivent rester lisibles.

---

## Task 4 : une page par épisode Seerah

**Fichiers**
- Créer : `seerah/001/index.html`
- Modifier : `seerah/index.html` (devient l'index de la série)

**Interfaces**
- *Consomme* : `.lecture` et `.lecture-ar` de la Task 3, la coquille de la Task 1.
- *Produit* : le **gabarit de page d'épisode**, que le chantier éditorial des épisodes 002 à
  005 reproduira tel quel.

⚠️ **Cette tâche ne construit aucun épisode nouveau.** Elle migre l'épisode déjà publié et
livre le gabarit. Les épisodes 002 à 005 sont un chantier éditorial séparé (§ 4 du spec).

- [ ] **Étape 1 : créer `seerah/001/index.html`**

Y déplacer le contenu de l'épisode 1 tel quel, dans `.lecture`. Le `<title>` doit être **propre
à l'épisode** — c'est lui qui s'affiche quand le lien est partagé sur WhatsApp :

```html
<title>Ses spécificités, partie 1 — La Vie du Prophète ﷺ | Yahdi Qalbah</title>
<meta name="description" content="Épisode 1 de la série Seerah, d'après Cheikh Dr. Yasir Qadhi. Les spécificités du Prophète Muhammad ﷺ.">
```

- [ ] **Étape 2 : transformer `seerah/index.html` en index**

Il ne contient plus le texte de l'épisode, mais la **liste des épisodes** (sombre, sélection) :

```html
<a class="episode-card" href="/seerah/001/">
  <span class="episode-num">Épisode 1</span>
  <h3>Ses spécificités — partie 1</h3>
</a>
```

Une entrée par épisode publié. **Ne pas y annoncer d'épisode non publié** : une carte qui mène
au vide coûte plus qu'elle ne rapporte.

- [ ] **Étape 3 : ajouter la reprise de lecture**

Dans `assets/site.js` (créé ici), mémoriser la position par épisode. **Confort pur** — sans JS,
la page reste entièrement lisible.

```js
// Reprise de lecture : une clé par page, aucune donnée personnelle.
(function () {
  var cle = "lecture:" + location.pathname;
  var y = parseInt(localStorage.getItem(cle) || "0", 10);
  if (y > 0) window.scrollTo(0, y);
  var minuteur;
  window.addEventListener("scroll", function () {
    clearTimeout(minuteur);
    minuteur = setTimeout(function () {
      localStorage.setItem(cle, String(window.scrollY));
    }, 300);
  });
})();
```

⚠️ **Le script ne sert à rien s'il n'est pas inclus.** Ajouter dans le `<head>` de **toutes** les
pages qui portent du texte long (`seerah/001/`, `noms/`, `prophetes/`) :

```html
<script src="/assets/site.js" defer></script>
```

`defer` est obligatoire : sans lui, le script s'exécute avant que la page existe et la reprise
de lecture ne trouve rien à faire défiler.

- [ ] **Étape 4 : vérification mécanique**

```bash
cd "E:/YAHDI QALBAH/prophetes-timeline"
test -f seerah/001/index.html && echo "épisode 1 migré"
# le script est réellement inclus là où il sert
grep -c 'assets/site.js' seerah/001/index.html noms/index.html prophetes/index.html
# attendu : 1 par fichier
grep -o "<title>[^<]*</title>" seerah/index.html seerah/001/index.html
# attendu : deux titres DIFFÉRENTS
grep -c "episode-card" seerah/index.html    # attendu : 1
```

- [ ] **Étape 5 : commit**

```bash
git add seerah/ assets/site.js
git commit -m "Seerah : une page par episode, index de serie, reprise de lecture"
git push origin main
```

- [ ] **Étape 6 : vérification par Saïbo (V5)**

> Envoie-toi `yahdiqalbah.com/seerah/001/` sur WhatsApp. **L'aperçu doit afficher le titre de
> l'épisode**, pas celui du site. C'est tout l'intérêt de la manœuvre : pouvoir envoyer un
> épisode précis.

---

## Task 5 : la page de participation

**Fichiers**
- Créer : `participer/index.html`
- Modifier : `assets/site.js` (bouton copier)

**Interfaces**
- *Consomme* : la coquille (Task 1), `.lecture` (Task 3).

🔴 **Bloquant avant mise en ligne** — deux éléments que seul Saïbo fournit : le **libellé
« sadaqa, pas zakat » validé par un savant**, et **les numéros à publier** (Wave / Orange Money)
plus le lien PayPal. **Ne pas inventer de numéro, ne pas mettre de valeur d'exemple** : un faux
numéro sur une page de don est le pire défaut possible. Si ces éléments manquent, construire la
page et **ne pas la pousser**.

- [ ] **Étape 1 : écrire la page**

Ordre imposé : ce que c'est (le contenu est gratuit et le restera, la participation ne débloque
aucun accès) → à quoi ça sert, exprimé en **coûts réels** (domaine pour une année, hébergement,
un micro pour le podcast, le temps d'un épisode de plus) → les moyens → les deux mentions
obligatoires → le bloc de transparence.

**Pas de paliers de montants.**

- [ ] **Étape 2 : les deux mentions obligatoires (V6)**

Elles doivent figurer littéralement :

1. Le libellé validé précisant qu'il s'agit d'une **sadaqa et non d'une zakat**.
2. « Les numéros ci-dessus sont les seuls. Nous ne sollicitons jamais de dons par message privé. »

- [ ] **Étape 3 : le bloc de transparence**

Présent **dès la mise en ligne**, même vide :

```html
<section class="transparence">
  <h2>À quoi a servi votre participation</h2>
  <p>Rien n'a encore été collecté à ce jour. Cette page sera mise à jour.</p>
</section>
```

- [ ] **Étape 4 : le bouton copier**

Ajouter à `assets/site.js`. Le numéro reste **visible en texte** : sans JS, on le lit et on le
recopie.

```js
// Bouton copier : le numéro est déjà lisible sans JS, ceci n'est qu'un confort.
document.querySelectorAll("[data-copier]").forEach(function (b) {
  b.addEventListener("click", function () {
    navigator.clipboard.writeText(b.dataset.copier).then(function () {
      var avant = b.textContent;
      b.textContent = "Copié";
      setTimeout(function () { b.textContent = avant; }, 1500);
    });
  });
});
```

- [ ] **Étape 5 : vérification mécanique**

```bash
cd "E:/YAHDI QALBAH/prophetes-timeline"
grep -ci "sadaqa" participer/index.html                        # attendu : ≥ 1
grep -c "jamais de dons par message privé" participer/index.html  # attendu : 1
grep -c "transparence" participer/index.html                   # attendu : ≥ 1
grep -ci "zakat" participer/index.html                         # attendu : ≥ 1 (la distinction)
```

- [ ] **Étape 6 : commit et mise en ligne**

```bash
git add participer/ assets/site.js
git commit -m "Page de participation : sadaqa jariya, moyens locaux et diaspora, transparence"
git push origin main
```

- [ ] **Étape 7 : vérification par Saïbo (V6 et V8)**

> Ouvre `yahdiqalbah.com/participer/`. **Vérifie chiffre par chiffre les numéros affichés** —
> c'est la seule page du site où une coquille coûte de l'argent à quelqu'un. Teste le bouton
> copier sur ton téléphone.

---

## Après ce plan

1. **Le chantier éditorial Seerah** — épisodes 002 à 005, un par un, dans le gabarit livré en
   Task 4. Le plus petit (002, 23 812 caractères) en premier.
2. **Le découpage des 99 Noms** en pages individuelles, en une passe mécanique.
3. Mettre à jour le compteur de l'accueil **à chaque publication** (critère V2).
