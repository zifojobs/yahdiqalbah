# Refonte du site Yahdi Qalbah — spécification de design

**Date** : 2026-08-08
**Dépôt** : `zifojobs/yahdiqalbah` (source : `E:\YAHDI QALBAH\prophetes-timeline\`)
**Statut** : en attente de relecture par Saïbo

---

## 1. Pourquoi maintenant

`yahdiqalbah.com` est en ligne depuis le 08/08/2026. Le site va donc commencer à être diffusé
— par WhatsApp d'abord, qui est le canal réel de Saïbo. La demande est de lui donner une
**allure institutionnelle**, en s'inspirant de la crédibilité de bayyinahtv.com.

⚠️ **Ce qu'on emprunte à Bayyinah TV est l'allure, pas la structure.** Bayyinah TV est une
plateforme vidéo payante avec un catalogue de centaines d'heures. Yahdi Qalbah est gratuit,
se lit, et compte trois espaces. Copier une navigation de catalogue mettrait le vide en
évidence au lieu de la qualité.

Ce document remplace le cadrage laissé en suspens dans
`brainstorms/2026-08-03-refonte-structure-site.md` (Q1 : « archi de l'info, visuel, ou les
deux ? » — la réponse est : **les deux**).

## 2. État des lieux, mesuré

| Page | Poids | Contenu | Navigation |
|---|---:|---|---|
| `index.html` | 14 Ko | hero, 4 cartes, 3 principes, pied | aucune |
| `noms/index.html` | **120 Ko** | les 52 notices, un seul fichier | aucune |
| `prophetes/index.html` | 57 Ko | les 25 récits, un seul fichier | aucune |
| `seerah/index.html` | 22 Ko | l'épisode 1 seul | aucune |

Faits établis par lecture des fichiers :

- **Aucune page ne contient de `<nav>`.** Chaque page est une île ; passer d'un espace à un
  autre oblige à repasser par l'accueil. C'est la cause principale de l'impression
  « collection de projets » plutôt qu'« institution ».
- La typographie est **déjà en variables partagées** (`--ar`, `--sans`, `--serif`) : le
  vocabulaire commun existe, il n'est simplement pas assemblé.
- Le CSS est **inliné dans chaque page**, donc dupliqué quatre fois.
- **Une seule URL par espace** ⇒ il est impossible de partager un épisode ou un Nom précis.
  C'est une limite sérieuse pour un site diffusé par partage de lien.

## 3. Décisions cadrées avec Saïbo

| # | Décision | Raison |
|---|---|---|
| D1 | On emprunte **l'allure institutionnelle**, pas la navigation par catalogue | Trois espaces ne remplissent pas un catalogue |
| D2 | **Refonte complète, page par page** | Choix de Saïbo ; la coquille d'abord pour ne pas bloquer la publication Seerah |
| D3 | **Sombre à l'entrée, clair à la lecture** | Les épisodes Seerah font 24 k à 74 k caractères ; l'or sur noir est éprouvant sur cette longueur |
| D4 | **Approche A** : feuille de style partagée, markup d'en-tête répété | Conserve « zéro dépendance, un fichier par page » ; pas d'étape de construction |
| D5 | **Bouton de participation** (sadaqa jariya) : Wave + Orange Money + PayPal **affichés**, sans intégration | Publiable tout de suite ; un agrégateur exigerait un compte marchand et le NINEA |

### Écartés, et pourquoi

- **Générateur statique** (Eleventy ou script de build) — plus de machinerie que de bénéfice
  pour 4 pages, et perte du « zéro dépendance » revendiqué au README.
- **Coquille injectée en JavaScript** — sans JS il n'y aurait plus de navigation du tout, et
  les moteurs ne la verraient pas. Rédhibitoire pour un public sur Android d'entrée de gamme.
- **Menu hamburger** — quatre liens ne justifient pas de les cacher, et il dépendrait du JS.
- **Paliers de montants** sur la page de don — transactionnel, mal accordé à une sadaqa.

## 4. Périmètre

**Dans le périmètre**

1. La coquille partagée (en-tête, navigation, pied de page, `assets/site.css`) sur les 4 pages.
2. L'accueil, traitement sombre.
3. Les pages de lecture, traitement clair.
4. Les pages de lecture en clair, appliquées aux **trois** espaces : `seerah/`, `noms/`,
   `prophetes/`.
5. La **structure d'URL par épisode** pour la Seerah (`seerah/002/`…) et le gabarit d'une page
   d'épisode, avec l'épisode 1 migré dedans comme cas de référence.
6. La page de participation (`participer/`).

**Hors périmètre, explicitement**

- 🔴 **La construction des épisodes Seerah 002 à 005.** C'est du **travail éditorial**
  (195 000 caractères à corriger et structurer, avec relecture obligatoire de Saïbo sur du
  contenu religieux), pas du design. Cette refonte livre la structure qui les accueillera ;
  les épisodes eux-mêmes font l'objet d'un chantier distinct, un épisode à la fois.
- **Le découpage des 99 Noms en pages individuelles.** Souhaitable, non urgent : la page tient
  encore à 52 notices. À reprendre en une passe mécanique après cette refonte.
- Le contenu lui-même : ni les 25 récits, ni les 52 notices, ni le texte de l'épisode 1 ne sont
  rouverts. La refonte touche la présentation, pas le fond.
- La maison du podcast et la page Cours d'arabe (pièces 4 et 5, non commencées).
- Toute intégration de paiement en ligne.

## 5. La coquille partagée

### En-tête

```
[logo] Yahdi Qalbah        Les Prophètes · Les 99 Noms · La Seerah    [ Participer ]
```

- Logo + nom à gauche, cliquables vers l'accueil.
- Les trois espaces au centre-droit ; **« Participer » détaché et en or** — seul appel à
  l'action du site.
- **Sur mobile, la navigation passe à la ligne.** Pas de hamburger (cf. § 3).
- **Non collant au défilement** : sur une page de 70 000 caractères lue au téléphone, une barre
  fixe consomme une bande d'écran en permanence pour un service rare.

### Pied de page

Trois blocs : **identité** (logo + une phrase sur l'institut) · **les espaces** (mêmes liens —
c'est là qu'on va quand on a fini de lire) · **sadaqa jariya** (contenu gratuit, participation
libre, lien vers `participer/`). Plus la mention des sources.

> Le contenu de Yahdi Qalbah est **intégralement sourcé**, et presque aucun site islamique
> francophone ne le montre. C'est le meilleur signal d'institution disponible : il doit être
> visible, pas discret.

### Technique

`assets/site.css` porte les couleurs, la typographie, l'en-tête, le pied et les boutons. Chaque
page conserve ensuite son CSS propre pour ce qui lui est spécifique. Le markup de l'en-tête
(≈15 lignes) est répété dans les 4 pages — accepté au titre de D4.

**Bénéfice mesurable** : le CSS commun, aujourd'hui inliné 4 fois, devient un fichier unique
mis en cache — donc **plus léger dès la deuxième page visitée**.

## 6. L'accueil — traitement sombre

**L'univers céleste existant est conservé.** Saïbo l'a validé en session (« extraordinaire ») ;
il est *discipliné* — plus sobre, plus d'espace noir autour — pas remplacé.

**Ordre de la page** : hero (nom de l'institut, verset 64:11 dont il tire son nom, une phrase
sur ce qu'on trouve ici) → les espaces → les trois engagements (sourcé · gratuit · passeur) →
participation, sobre → pied de page.

**La participation vient après les engagements**, jamais avant : on demande une fois qu'on a donné.

### Le changement le plus rentable : afficher les volumes

Les cartes portent le volume réel du fonds :

> **La Chaîne des Prophètes** — 25 récits sourcés
> **Les 99 Noms d'Allah** — 52 notices publiées
> **La Vie du Prophète ﷺ** — la série, épisode par épisode

Le site a beaucoup plus de contenu qu'il n'en laisse voir. Ces chiffres font comprendre en
trois secondes qu'il s'agit d'un travail de fond. **Annoncer « 52 sur 99 » est plus crédible
que de le taire** : cela dit que le travail avance et qu'il est tenu.

Ces nombres sont écrits en dur dans le HTML et **doivent être mis à jour à chaque publication**
(voir § 10, critère V6).

## 7. Les pages de lecture — traitement clair

- **Fond crème chaud**, jamais blanc pur : moins d'éblouissement, et l'or y survit comme accent.
- **Largeur de ligne bornée à ~65 caractères.** C'est la mesure qui décide qu'on finit ou non un
  texte de 70 000 signes — plus déterminante que le choix de la police.
- **Serif pour le corps**, interligne généreux, taille confortable au pouce.
- **Arabe traité à part** : versets et hadiths plus grands, en RTL, visuellement détachés,
  jamais noyés dans le paragraphe français.
- **Sources en fin de section**, visibles.
- **Reprise de lecture** : la position est mémorisée localement (`localStorage`) par épisode.
  Confort pur — sans JavaScript, la page reste entièrement lisible.

### Une page par épisode Seerah

`seerah/` devient l'index (sombre, sélection) ; chaque épisode vit sous `seerah/00N/` avec son
URL, son titre et son aperçu de partage.

**Motif** : les épisodes 002 à 005 totalisent 195 000 caractères. Versés dans le fichier
unique actuel, `seerah/index.html` passerait de 22 Ko à ~250 Ko — une page abandonnée avant
affichage sur un Android d'entrée de gamme en réseau faible. Et sans URL propre, Saïbo ne peut
pas envoyer un épisode précis par WhatsApp, qui est son canal de diffusion.

## 8. La page de participation (`participer/`)

**Ton** : une seule demande, énoncée une fois, sans insistance ni culpabilisation. La page
s'ouvre sur le fait que **le contenu est gratuit et le restera** — la participation ne débloque
aucun accès. C'est ce qui distingue une sadaqa d'un abonnement déguisé.

**Pas de paliers de montants.** À la place, le coût réel des choses — le domaine pour une année,
l'hébergement, un micro pour enregistrer le podcast, le temps de produire un épisode de plus.
Chacun se situe seul, et la promesse d'usage devient vérifiable.

**Moyens** : numéros Wave et Orange Money avec bouton **copier** (personne ne recopie un numéro
à la main sur un téléphone) ; lien PayPal pour la diaspora.

**Mentions obligatoires**

1. « Il s'agit d'une **sadaqa**, pas d'une zakat. » 🔴 **Libellé à faire confirmer par un savant
   avant mise en ligne** — la zakat a des bénéficiaires définis, et quelqu'un qui croirait s'en
   acquitter ici pourrait ne pas l'avoir accomplie. *(Aucun avis de fiqh n'est rendu dans ce
   document.)*
2. « Les numéros ci-dessus sont les seuls. Nous ne sollicitons jamais de dons par message
   privé. » — les projets religieux qui collectent sont couramment usurpés.

**Bloc « à quoi a servi votre participation »**, daté, présent **dès la mise en ligne** même
vide (« rien n'a encore été collecté »). La transparence commence avant le premier don, sinon
elle ne commence jamais. La promesse faite est une **amāna**.

## 9. Contraintes non négociables

### Image et contenu religieux

- **Jamais le Nom d'Allah en décor**, filigrane ou texture de fond. S'il apparaît, il domine la
  page. *(C'est la faute qui a arrêté le test de v1 le 04/08.)*
- **Décor strictement non figuratif** : géométrie islamique (étoile à huit branches, entrelacs)
  en SVG, aucun être vivant, jamais le Prophète ﷺ ni les compagnons.
- **Le ghayb ne s'illustre pas.**
- Registre **contemplatif d'adulte** — aucune mascotte, rien de ludique, même bien exécuté.
- **Aucune image générée par IA** : construction en code pur (SVG/CSS). Décidé le 03/08 et
  confirmé — le skill Higgsfield de cet environnement demande une authentification interactive
  impossible en session.

### Technique

- Zéro dépendance externe, aucune étape de construction.
- **La navigation fonctionne sans JavaScript.** Le JS n'est admis que pour du confort
  (reprise de lecture, bouton copier).
- Public cible : **Android d'entrée de gamme, réseau faible, Sénégal et diaspora**. Toute
  décision se tranche de ce point de vue.
- Interface et contenu en français.

## 10. Ordre de construction et critères de vérification

La coquille vient en premier parce qu'elle est prérequis à tout le reste — et parce qu'ainsi
**la publication des épisodes Seerah n'est jamais bloquée** : ils sortent dans l'état où leur
page se trouve.

| # | Étape | Vérification |
|---|---|---|
| 1 | `assets/site.css` + en-tête/pied sur les 4 pages | **V1** — depuis n'importe quelle page, on atteint les 3 autres en un clic, **JavaScript désactivé** |
| 2 | Accueil, traitement sombre + volumes affichés | **V2** — les 3 volumes affichés correspondent au contenu réellement en ligne |
| 3 | Gabarit de lecture clair, appliqué aux **3** espaces (`seerah/`, `noms/`, `prophetes/`) | **V3** — largeur de ligne ≤ 65 caractères sur mobile ; **V4** — les 3 pages restent lisibles avec JS désactivé |
| 4 | Structure `seerah/00N/` + épisode 1 migré comme cas de référence | **V5** — `seerah/001/` a son URL propre, partageable, avec son titre, et `seerah/` devient l'index |
| 5 | `participer/` | **V6** — les deux mentions obligatoires du § 8 sont présentes |

⚠️ **L'étape 4 ne construit aucun épisode nouveau** : elle livre le gabarit et migre l'épisode
déjà publié. Les épisodes 002 à 005 sont un chantier éditorial distinct (§ 4).

**Vérification transverse V7** : aucune page ne dépasse **150 Ko**. C'est le garde-fou qui
protège le public réel ; `noms/index.html` (120 Ko) est déjà proche et sortira du périmètre
avec son propre découpage.

**Vérification finale V8** : contrôle en direct après déploiement sur `yahdiqalbah.com`, pas sur
le fichier local — règle permanente de Saïbo. **Le rendu visuel est jugé par Saïbo dans son
navigateur**, pas par capture d'écran.

## 11. Actions qui n'appartiennent qu'à Saïbo

- 🔴 **Faire valider le libellé « sadaqa, pas zakat » par un savant** avant la mise en ligne de
  `participer/`.
- 🔴 **Choisir le numéro à publier.** Publier son numéro Wave, c'est publier son numéro personnel
  sur le web ouvert : il sera aspiré. Utiliser un second numéro s'il en a un. **À terme, le
  NINEA (en cours chez Rayana) permettra un compte Wave professionnel** — reçus émis, numéro
  dédié : c'est la bonne version.
- Fournir le lien PayPal.
- Trancher `yahdiqalbah.com` vs `www.yahdiqalbah.com` en domaine principal **avant la première
  diffusion** (Vercel → Domains → *Set as primary*). Un lien diffusé ne se rattrape pas.
