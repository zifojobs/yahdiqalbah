/* Yahdi Qalbah — confort de lecture.
   Tout ce qui vit ici est facultatif : sans JavaScript, les pages restent
   entierement navigables et les textes entierement lisibles. */

/* Reprise de lecture : une cle par page, aucune donnee personnelle,
   rien qui sorte du telephone. */
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

/* Bouton copier : le numero est deja lisible en clair a cote,
   ceci n'est qu'un confort pour ne pas le recopier a la main. */
document.querySelectorAll("[data-copier]").forEach(function (b) {
  b.addEventListener("click", function () {
    navigator.clipboard.writeText(b.dataset.copier).then(function () {
      var avant = b.textContent;
      b.textContent = "Copié";
      setTimeout(function () { b.textContent = avant; }, 1500);
    });
  });
});
