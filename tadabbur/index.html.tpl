<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tadabbur — Institut Yahdi Qalbah</title>
<meta name="description" content="Un verset, et ce qu'il change aujourd'hui. Le tadabbur, c'est méditer le Coran jusqu'à ce qu'il touche la journée ordinaire — le travail, la fatigue, la reconnaissance.">
<meta property="og:title" content="Tadabbur — Institut Yahdi Qalbah">
<meta property="og:description" content="Un verset, et ce qu'il change aujourd'hui.">
<meta property="og:type" content="article">
<meta property="og:image" content="https://yahdiqalbah.com/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Institut Yahdi Qalbah - Enseigner et faire aimer le Coran">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600&family=Amiri:wght@400;700&display=swap" rel="stylesheet">
<link rel="canonical" href="https://yahdiqalbah.com/tadabbur/">
<meta property="og:url" content="https://yahdiqalbah.com/tadabbur/">
<link rel="stylesheet" href="/assets/site.css">
<style>
:root{
  --noir:#0D0B07; --noir-2:#161209; --or:#C9A962; --or-vif:#E8D5A3; --or-sombre:#8a7038;
  --creme:#F5EEDF; --muted:#9c937e; --line:rgba(201,169,98,.25);
  --serif:'Cormorant Garamond',serif; --sans:'Plus Jakarta Sans',sans-serif; --ar:'Amiri',serif;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--noir);color:var(--creme);font-family:var(--sans);font-weight:300;line-height:1.7;overflow-x:hidden}
::selection{background:var(--or);color:var(--noir)}
::-webkit-scrollbar{width:9px}
::-webkit-scrollbar-track{background:var(--noir)}
::-webkit-scrollbar-thumb{background:linear-gradient(var(--or-sombre),var(--or));border-radius:99px}
#stars{position:fixed;inset:0;z-index:0;pointer-events:none}
.wrap{position:relative;z-index:1}
a{color:var(--or);text-decoration:none}

header.hero{text-align:center;padding:7rem 1.5rem 3rem;max-width:820px;margin:0 auto}
@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
header.hero>*{animation:fadeUp 1s cubic-bezier(.16,1,.3,1) both}
.kicker{font-size:.72rem;letter-spacing:.35em;text-transform:uppercase;color:var(--muted)}
.hero .ha{animation-delay:.15s;font-family:var(--ar);font-size:clamp(1.8rem,5vw,2.8rem);color:var(--or);line-height:1.9;margin-top:.6rem}
h1{animation-delay:.3s;font-family:var(--serif);font-weight:600;font-size:clamp(2.2rem,6vw,4rem);line-height:1.05;
  background:linear-gradient(110deg,var(--creme) 15%,var(--or) 40%,var(--or-vif) 50%,var(--or) 60%,var(--creme) 85%);
  background-size:220% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;
  animation:fadeUp 1s cubic-bezier(.16,1,.3,1) .3s both,shimmer 9s ease-in-out 2s infinite}
@keyframes shimmer{0%,100%{background-position:0% 0}50%{background-position:100% 0}}
.hero p.sub{animation-delay:.45s;margin:1.4rem auto 0;max-width:56ch;color:var(--muted)}
.ep-badge{animation-delay:.6s;display:inline-block;margin-top:1.6rem;font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;
  border:1px solid var(--line);padding:.5rem 1.1rem;border-radius:999px;color:var(--or)}

/* ---------- CE QU'EST LE TADABBUR ---------- */
.intro{max-width:720px;margin:0 auto;padding:0 1.5rem 1rem}
.intro .fondement{border:1px solid var(--line);border-radius:18px;padding:1.8rem 1.7rem;
  background:linear-gradient(160deg,rgba(26,20,9,.6),rgba(15,12,6,.45));text-align:center}
.intro .fondement .v-ar{font-family:var(--ar);font-size:clamp(1.35rem,4.4vw,1.9rem);color:var(--or-vif);line-height:2.1}
.intro .fondement .v-fr{font-family:var(--serif);font-style:italic;font-size:1.12rem;color:var(--creme);margin-top:1rem}
.intro .fondement .v-ref{font-size:.74rem;letter-spacing:.2em;text-transform:uppercase;color:var(--or-sombre);margin-top:.9rem}
.intro > p{font-size:1.02rem;color:#dcd3bd;margin-top:1.4rem}

/* ---------- INDEX DE LA SERIE ---------- */
.episodes{max-width:720px;margin:0 auto;padding:1rem 1.5rem 4rem;display:grid;gap:1rem}
.episode-card{display:block;border:1px solid var(--line);border-radius:18px;padding:1.6rem 1.7rem;
  background:linear-gradient(160deg,rgba(26,20,9,.6),rgba(15,12,6,.45));
  transition:border-color .3s,transform .3s,box-shadow .3s}
.episode-card:hover{border-color:var(--or);transform:translateY(-3px);box-shadow:0 16px 44px rgba(0,0,0,.45)}
.episode-num{font-size:.68rem;letter-spacing:.28em;text-transform:uppercase;color:var(--or-sombre)}
.episode-card h3{font-family:var(--serif);font-weight:600;font-size:1.5rem;color:var(--creme);
  line-height:1.15;margin-top:.35rem}
.episode-card .card-ar{font-family:var(--ar);font-size:1.15rem;color:var(--or);margin-top:.5rem;line-height:1.9}
.episode-card p{font-size:.9rem;color:var(--muted);margin-top:.6rem}

.next-ep{max-width:720px;margin:0 auto 4rem;padding:0 1.5rem}
.next-ep p{font-size:.9rem;color:var(--muted);text-align:center;font-style:italic;font-family:var(--serif)}

footer{padding:3rem 1.5rem 3rem;text-align:center;font-size:.78rem;color:var(--muted);
  border-top:1px solid rgba(201,169,98,.14)}
footer .f-ar{font-family:var(--ar);font-size:1.5rem;color:var(--or)}
footer .flogo{font-family:var(--serif);font-size:1.1rem;color:var(--or);margin-top:.3rem}
footer .fnote{max-width:62ch;margin:.8rem auto 0}

@media (max-width:760px){ header.hero{padding-top:5.5rem} }
@media (prefers-reduced-motion:reduce){ *{animation:none!important;transition:none!important} }
</style>
</head>
<body>
<header class="site-header">
  <a class="site-brand" href="/">
    <img src="/assets/logo.png" alt="" width="36" height="36">
    <span>Yahdi Qalbah</span>
  </a>
  <nav class="site-nav" aria-label="Espaces">
    <a href="/prophetes/">Les Prophètes</a>
    <a href="/noms/">Les 99 Noms</a>
    <a href="/seerah/">La Seerah</a>
    <a href="/tadabbur/" aria-current="page">Tadabbur</a>
    <a href="/participer/" class="btn-or">Participer</a>
  </nav>
</header>
<canvas id="stars" aria-hidden="true"></canvas>

<div class="wrap">
<header class="hero">
  <p class="kicker">Institut Yahdi Qalbah</p>
  <p class="ha" lang="ar" dir="rtl">تَدَبُّر</p>
  <h1>Un verset, et ce qu'il change aujourd'hui</h1>
  <p class="sub">Le tadabbur, ce n'est pas lire le Coran. C'est le laisser descendre jusque dans la journée ordinaire — le travail, la fatigue, la reconnaissance qu'on oublie de dire.</p>
  <span class="ep-badge">5 versets médités</span>
</header>

<div class="intro">
  <div class="fondement">
    <p class="v-ar" lang="ar" dir="rtl">أَفَلَا يَتَدَبَّرُونَ ٱلْقُرْءَانَ أَمْ عَلَىٰ قُلُوبٍ أَقْفَالُهَآ</p>
    <p class="v-fr">« Ne méditent-ils pas sur le Coran ? Ou y a-t-il des cadenas sur leurs cœurs ? »</p>
    <p class="v-ref">Sourate Muhammad, 47 : 24</p>
  </div>
  <p>C'est le Coran lui-même qui donne son nom à cet espace. <i>Tadabbur</i> — méditer un verset,
  le retourner, le laisser travailler. Pas pour en tirer une règle, mais pour qu'il change quelque
  chose à la journée qui commence.</p>
  <p>Ici, un verset à la fois. Le texte arabe et sa traduction, ce que le verset ouvre quand on
  s'arrête dessus, et une chose à faire aujourd'hui — pas demain, pas un jour.</p>

  <p>Depuis le troisième verset s'ajoute une note <strong>« Dans la langue »</strong> : ce qu'une
  forme arabe — une lettre, une place dans la phrase, une racine — porte de sens que la
  traduction ne peut pas montrer. On y décrit la forme ; on n'y propose jamais une traduction
  concurrente à celle qui est citée.</p>
</div>

<div class="episodes">
  <a class="episode-card" href="/tadabbur/001/">
    <span class="episode-num">Verset 1 · Sourate At-Takathur 102 : 8</span>
    <h3>Le wifi qui marche bien</h3>
    <p class="card-ar" lang="ar" dir="rtl">@@AR:102:8@@</p>
    <p>Le dernier verset d'une sourate sur l'accumulation. Ce qui sera demandé n'est pas ce qu'on a raté — c'est ce dont on a profité.</p>
  </a>
  <a class="episode-card" href="/tadabbur/002/">
    <span class="episode-num">Verset 2 · Sourate Yunus 10 : 58</span>
    <h3>De quoi se réjouir vraiment</h3>
    <p class="card-ar" lang="ar" dir="rtl">@@S:10:58:0:6@@</p>
    <p>Un contrat signé, un salaire qui arrive : la joie est légitime. Le verset ne l'interdit pas — il déplace ce qui la mérite le plus.</p>
  </a>
  <a class="episode-card" href="/tadabbur/003/">
    <span class="episode-num">Verset 3 · Sourate Al-Anfâl 8 : 11</span>
    <h3>La pluie n'était pas pour la terre</h3>
    <p class="card-ar" lang="ar" dir="rtl">@@S:8:11:7:12@@</p>
    <p>À Badr, le Coran ne dit pas qu'il a plu. Il dit ce que la pluie était venue faire &mdash; et une seule lettre suffit à le dire.</p>
  </a>
  <a class="episode-card" href="/tadabbur/004/">
    <span class="episode-num">Verset 4 · Sourate Al-Kahf 18 : 82</span>
    <h3>Une lettre qui attend que tu grandisses</h3>
    <p class="card-ar" lang="ar" dir="rtl">@@S:18:82:8:11@@</p>
    <p>Le mur ne tenait pas : il attendait. Entre le début et la fin du verset, le trésor change de nom.</p>
  </a>
  <a class="episode-card" href="/tadabbur/005/">
    <span class="episode-num">Verset 5 · Sourate Al-Baqarah 2 : 35</span>
    <h3>Habite</h3>
    <p class="card-ar" lang="ar" dir="rtl">@@S:2:35:2:6@@</p>
    <p>Le premier ordre donné au premier homme n'est pas un ordre de faire. Et sa racine est celle de la tranquillité.</p>
  </a>
</div>

<div class="next-ep"><p>Un verset paraît quand il est médité et vérifié — jamais avant.</p></div>

<footer>
  <p class="f-ar" lang="ar">@@S:38:29:0:6@@</p>
  <p class="flogo">Institut Yahdi Qalbah</p>
  <p class="fnote">Toutes les traductions françaises de ce site sont celles de Muhammad Hamidullah, reprises telles quelles.</p>
</footer>
</div>

<script>
const cv=document.getElementById("stars"),cx=cv.getContext("2d");
let stars=[];
function resize(){cv.width=innerWidth;cv.height=innerHeight;
  stars=Array.from({length:Math.min(170,innerWidth/8)},()=>({
    x:Math.random()*cv.width,y:Math.random()*cv.height,
    r:Math.random()*1.3+.3,p:Math.random()*Math.PI*2,s:.4+Math.random()*.8}));
}
resize();addEventListener("resize",resize);
const reduced=matchMedia("(prefers-reduced-motion: reduce)").matches;
function draw(t){
  cx.clearRect(0,0,cv.width,cv.height);
  for(const st of stars){
    const a=.25+.45*Math.abs(Math.sin(t/1600*st.s+st.p));
    cx.beginPath();cx.arc(st.x,st.y,st.r,0,7);
    cx.fillStyle=`rgba(232,213,163,${a})`;cx.fill();
  }
  if(!reduced)requestAnimationFrame(draw);
}
requestAnimationFrame(draw);
</script>

<footer class="site-footer">
  <div class="site-footer-inner">
    <div>
      <h2>Institut Yahdi Qalbah</h2>
      <p>Enseigner et faire aimer le Coran — Sénégal &amp; diaspora francophone.</p>
      <p class="site-footer-contact"><a href="https://wa.me/221775277164">WhatsApp</a> · <a href="mailto:yahdiqalbahinstitute@gmail.com">yahdiqalbahinstitute@gmail.com</a></p>
    </div>
    <div>
      <h2>Les espaces</h2>
      <ul>
        <li><a href="/prophetes/">La Chaîne des Prophètes</a></li>
        <li><a href="/noms/">Les 99 Noms d’Allah</a></li>
        <li><a href="/seerah/">La Vie du Prophète ﷺ</a></li>
        <li><a href="/tadabbur/">Tadabbur</a></li>
      </ul>
    </div>
    <div>
      <h2>Sadaqa jariya</h2>
      <p>Tout le contenu est gratuit et le restera. La participation est libre et ne débloque aucun accès.</p>
      <p><a href="/participer/">Participer →</a></p>
    </div>
  </div>
  <p class="site-footer-sources">Chaque affirmation de ce site renvoie à ses sources — Coran, hadiths et ouvrages cités.</p>
</footer>
</body>
</html>
