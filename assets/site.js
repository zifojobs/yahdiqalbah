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
