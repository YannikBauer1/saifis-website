/* Shared by every page: header state, small video loops, the inquiry form. */
(function () {
  ScrollCraft.mount(document.body);

  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Pinned sections get their height from script, so Safari can miss a #section link on load. */
  if (location.hash.length > 1) {
    var target = document.getElementById(location.hash.slice(1));
    var land = function () { if (target) target.scrollIntoView({ behavior: 'instant' }); };
    requestAnimationFrame(land);
    addEventListener('load', function () { setTimeout(land, 80); });
  }

  /* ------------------------------------------------- header: solid over dark -- */
  (function () {
    var bar = document.querySelector('.bar'), quiet = document.querySelector('.quiet');
    var peak = document.querySelector('.peak'), close = document.querySelector('.close');
    function tick() {
      var y = bar.offsetTop + bar.offsetHeight, h = innerHeight;   // not moved by the slide-away below
      var overHero = quiet && quiet.getBoundingClientRect().top + h * .37 > y;
      var p = peak && peak.getBoundingClientRect();
      var overFilm = p && matchMedia('(max-width: 860px), (max-width: 1100px) and (orientation: portrait)').matches && p.top < y && p.bottom > 0;   // full-bleed on phones
      var overEnd = close.getBoundingClientRect().top < y;
      bar.classList.toggle('is-solid', overHero || overFilm || overEnd);
      slide();
    }

    /* Phones: the header leaves when you scroll down and comes back when you scroll up. */
    var compact = matchMedia('(max-width: 900px)'), root = document.documentElement, lastY = scrollY;
    function away(v) { bar.classList.toggle('is-away', v); root.classList.toggle('bar-away', v); }
    function slide() {
      var now = scrollY, end = root.scrollHeight - innerHeight;
      if (!compact.matches || now <= bar.offsetHeight) { away(false); lastY = now; return; }
      if (now >= end) { lastY = end; return; }        // the bounce at the bottom of the page is not a scroll up
      if (Math.abs(now - lastY) < 8) return;         // ignore a resting finger
      away(now > lastY); lastY = now;
    }
    bar.addEventListener('focusin', function () { away(false); });
    addEventListener('scroll', tick, { passive: true });
    addEventListener('resize', tick);
    tick();

    /* The end card has both buttons itself: the bottom bar steps aside while they are on screen. */
    var dock = document.querySelector('.dock'), cta = document.querySelector('.card__cta');
    if (dock && cta && window.IntersectionObserver) {
      new IntersectionObserver(function (e) { dock.classList.toggle('is-away', e[0].isIntersecting); }, { rootMargin: '0px 0px -80px 0px' }).observe(cta);
    }
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
