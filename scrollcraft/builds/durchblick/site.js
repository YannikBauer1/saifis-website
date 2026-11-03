/* Shared by every page: header state, small video loops, the inquiry form. */
(function () {
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ------------------------------------------------- header: solid over dark -- */
  (function () {
    var bar = document.querySelector('.bar'), quiet = document.querySelector('.quiet');
    var peak = document.querySelector('.peak'), close = document.querySelector('.close');
    function tick() {
      var y = bar.getBoundingClientRect().bottom, h = innerHeight;
      var overHero = quiet && quiet.getBoundingClientRect().top + h * .37 > y;
      var p = peak && peak.getBoundingClientRect();
      var overFilm = p && innerWidth <= 860 && p.top < y && p.bottom > 0;   // full-bleed on phones
      var overEnd = close.getBoundingClientRect().top < y;
      bar.classList.toggle('is-solid', overHero || overFilm || overEnd);
    }
    addEventListener('scroll', tick, { passive: true });
    addEventListener('resize', tick);
    tick();
  })();

  /* ------------------------------------------- small loops only when seen -- */
  document.querySelectorAll('video[data-loop]').forEach(function (v) {
    if (reduce) return;
    new IntersectionObserver(function (e) {
      if (e[0].isIntersecting) { var t = v.play(); if (t && t.catch) t.catch(function () {}); } else v.pause();
    }, { threshold: .25 }).observe(v);
  });

  /* ------------------------------------------------------------- inquiry -- */
  var dlg = document.getElementById('anfrage');
  if (dlg && dlg.showModal) {
    document.querySelectorAll('[data-anfrage]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        var obj = a.getAttribute('data-objekt'), svc = a.getAttribute('data-leistung');
        if (obj) dlg.querySelector('[name=Objekt]').value = obj;
        if (svc) dlg.querySelector('[name=Anliegen]').value = svc;
        dlg.showModal();
      });
    });
    dlg.querySelector('[data-close]').addEventListener('click', function () { dlg.close(); });
    dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
    var form = dlg.querySelector('[data-form]'), status = dlg.querySelector('[data-status]');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form), lines = ['Guten Tag,', '', 'ich möchte einen kostenfreien Analyse-Termin anfragen.', ''];
      d.forEach(function (v, k) { if (String(v).trim()) lines.push(k + ': ' + v); });
      var href = 'mailto:info@saifis-gebaeudereinigung.de?subject=' + encodeURIComponent('Anfrage Analyse-Termin') + '&body=' + encodeURIComponent(lines.join('\n'));
      status.textContent = 'Ihr E-Mail-Programm sollte sich jetzt öffnen. Falls nicht, erreichen Sie uns unter 0971 12382990.';
      status.hidden = false;
      window.location.href = href;
    });
  }
})();
