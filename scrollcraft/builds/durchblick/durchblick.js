/* The S in the glass. Page-local: the engine is untouched.
   A procedural film of dried water, grime and old smears sits on the visitor's
   own pane. Scroll drags a squeegee along the fan path, and that path is the
   S of Saifi's logo. */
(function () {
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var clamp = function (v, a, b) { return Math.min(b, Math.max(a, v)); };
  var range = function (p, a, b) { return clamp((p - a) / (b - a), 0, 1); };
  var smooth = function (t) { return t * t * (3 - 2 * t); };

  // Seeded, so scrubbing back and forth always shows the same glass.
  function rng(seed) {
    return function () {
      seed |= 0; seed = seed + 0x6D2B79F5 | 0;
      var t = Math.imul(seed ^ seed >>> 15, 1 | seed);
      t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
  }

  /* ----------------------------------------------------------- the film -- */
  function makeFilm(w, h, k) {
    var r = rng(77);
    var c = document.createElement('canvas'); c.width = w; c.height = h;
    var x = c.getContext('2d');
    // Upright phones look at bright sky through the film, so the dirt gets a little weight.
    if (h > w && w / k <= 760) { x.fillStyle = 'rgba(66,68,64,.24)'; x.fillRect(0, 0, w, h); }

    // Soft layers are painted small and scaled up: the blur costs nothing and
    // works on browsers without canvas filters.
    function soft(scale, paint) {
      var s = document.createElement('canvas');
      s.width = Math.ceil(w / scale); s.height = Math.ceil(h / scale);
      paint(s.getContext('2d'), s.width, s.height);
      x.imageSmoothingEnabled = true; x.imageSmoothingQuality = 'high';
      x.drawImage(s, 0, 0, w, h);
    }

    // Haze: uneven, never a flat veil. This is what the sun catches.
    soft(26, function (g, W, H) {
      g.fillStyle = 'rgba(203,218,231,.22)'; g.fillRect(0, 0, W, H);
      for (var i = 0; i < 90; i++) {
        var px = r() * W, py = r() * H, rad = (.06 + r() * .22) * Math.max(W, H);
        var gr = g.createRadialGradient(px, py, 0, px, py, rad);
        var a = .04 + r() * .13;
        gr.addColorStop(0, 'rgba(226,235,243,' + a + ')'); gr.addColorStop(1, 'rgba(226,235,243,0)');
        g.fillStyle = gr; g.fillRect(0, 0, W, H);
      }
    });

    // Grime that settled: heavier toward the bottom and the corners, cold and grey-brown.
    soft(18, function (g, W, H) {
      var low = g.createLinearGradient(0, H * .5, 0, H);
      low.addColorStop(0, 'rgba(116,116,108,0)'); low.addColorStop(1, 'rgba(116,116,108,.2)');
      g.fillStyle = low; g.fillRect(0, 0, W, H);
      for (var i = 0; i < 46; i++) {
        var px = r() * W, py = H * (.15 + r() * .9), rad = (.03 + r() * .1) * Math.max(W, H);
        var gr = g.createRadialGradient(px, py, 0, px, py, rad);
        gr.addColorStop(0, 'rgba(104,106,100,' + (.04 + r() * .1) + ')'); gr.addColorStop(1, 'rgba(104,106,100,0)');
        g.fillStyle = gr; g.fillRect(0, 0, W, H);
      }
    });

    // Somebody's last attempt with a dirty cloth: wide faint arcs.
    soft(5, function (g, W, H) {
      g.lineCap = 'round';
      for (var i = 0; i < 26; i++) {
        var cx = r() * W, cy = r() * H, R = (.1 + r() * .34) * Math.max(W, H), s = r() * 6.28;
        g.strokeStyle = 'rgba(236,243,248,' + (.018 + r() * .05) + ')';
        g.lineWidth = (6 + r() * 16);
        g.beginPath(); g.arc(cx, cy, R, s, s + .5 + r() * 1.2); g.stroke();
      }
    });

    // Rain runs: the signature of a neglected pane. Gravity-straight, wandering a little.
    x.lineCap = 'round';
    var runs = Math.round(w * h / (1500 * k * k) * .7);
    for (var i = 0; i < runs; i++) {
      var px = r() * w, py = -40 + r() * h * .94, len = (24 + Math.pow(r(), 2.2) * 340) * k;
      var bright = r() > .28;
      x.strokeStyle = bright ? 'rgba(238,244,249,' + (.035 + r() * .15) + ')' : 'rgba(84,88,84,' + (.03 + r() * .13) + ')';
      x.lineWidth = (.45 + r() * 1.5) * k;
      x.beginPath(); x.moveTo(px, py);
      var cx = px, cy = py;
      while (cy < py + len) { cy += (14 + r() * 30) * k; cx += (r() - .5) * 2.4 * k; x.lineTo(cx, cy); }
      x.stroke();
      if (r() > .72) { // the bead of dirt at the end of a run
        x.fillStyle = bright ? 'rgba(240,245,250,.2)' : 'rgba(78,80,74,.28)';
        x.beginPath(); x.arc(cx, cy, (.8 + r() * 1.5) * k, 0, 6.3); x.fill();
      }
    }

    // Dried water spots, in clusters, each one a pale ring.
    var clusters = 54;
    for (var c1 = 0; c1 < clusters; c1++) {
      var ox = r() * w, oy = r() * h, spread = (30 + r() * 150) * k, n = 18 + r() * 70;
      for (var j = 0; j < n; j++) {
        var a = r() * 6.28, d = Math.pow(r(), 1.6) * spread, rad = (.5 + Math.pow(r(), 3) * 5) * k;
        var sx = ox + Math.cos(a) * d, sy = oy + Math.sin(a) * d, st = r() * 6.28;
        x.beginPath(); x.ellipse(sx, sy, rad * (.75 + r() * .5), rad * (.75 + r() * .5), r() * 3, 0, 6.3);
        x.fillStyle = 'rgba(232,240,246,' + (.012 + r() * .04) + ')'; x.fill();
        x.beginPath(); x.ellipse(sx, sy, rad, rad * (.8 + r() * .3), r() * 3, st, st + 2 + r() * 3.4);
        x.strokeStyle = 'rgba(243,247,251,' + (.03 + r() * .13) + ')'; x.lineWidth = .5 * k; x.stroke();
      }
    }

    // Dust and fly specks, the only truly dark marks.
    var specks = Math.round(w * h / (620 * k * k));
    for (var s = 0; s < specks; s++) {
      x.fillStyle = 'rgba(52,48,42,' + (.14 + r() * .42) + ')';
      x.beginPath(); x.arc(r() * w, r() * h, (.28 + Math.pow(r(), 3) * 1.25) * k, 0, 6.3); x.fill();
    }
    return c;
  }

  /* -------------------------------------------------- the path: Saifi's S -- */
  // The mark, traced from the logo file: two bars, two folded triangles. The
  // clean glass is exactly this silhouette from the first pixel, so the dirty
  // film around it never changes shape, it just stays where it is.
  var MARK = {
    top: [[207, 32], [640, 32], [542, 167], [107, 167]],
    foldA: [[107, 167], [322, 167], [213, 316]],
    foldB: [[449, 244], [555, 391], [340, 391]],
    low: [[121, 391], [555, 391], [456, 527], [21, 527]]
  };
  var X0 = 21, X1 = 640, Y0 = 32, Y1 = 527, RATIO = (X1 - X0) / (Y1 - Y0);
  // The logo's lean: from the vertical, along the slanted edges.
  var LEAN = Math.atan2(109, 149), SLOPE = 109 / 149;

  function buildPath(W, H, copyBottom) {
    var wide = W >= 1000 && W / H > 1, sideways = !wide && W > H && H <= 520, bw, bh, ox, oy;
    if (sideways) {
      bh = Math.min(H - 150, W * .46 / RATIO); bw = bh * RATIO;
      ox = W * .975 - bw; oy = 76 + (H - 150 - bh) / 2;
    } else if (wide) {
      bh = Math.min(H * .7, W * .5 / RATIO); bw = bh * RATIO;
      ox = W * .96 - bw; oy = H * .95 - bh;
    } else {
      var phone = W <= 760, gap = phone ? 12 : 16;
      var room = Math.min(H, innerHeight) - copyBottom - gap - (phone ? 72 : W <= 900 ? 84 : 32);   // the address bar may be covering the bottom
      bw = Math.min(W * (phone ? .92 : .86), room * RATIO); bh = bw / RATIO;
      ox = (W - bw) / 2; oy = copyBottom + gap + (room - bh) / 2;
    }
    var u = bh / (Y1 - Y0);
    function at(p) { return [ox + (p[0] - X0) * u, oy + (p[1] - Y0) * u]; }
    var out = [];
    var angs = [];
    function line(a, b, n, ang) { for (var i = 0; i < n; i++) { var t = i / n; out.push([a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t]); angs.push(ang); } }
    function bend(a, c, b, from, to) { for (var t = 0; t < 1; t += 1 / 18) { var v = 1 - t; out.push([v * v * a[0] + 2 * v * t * c[0] + t * t * b[0], v * v * a[1] + 2 * v * t * c[1] + t * t * b[1]]); angs.push(from + (to - from) * t); } }

    // Every slanted edge in the logo leans the same way, so the blade does too.
    // It starts and ends flush with each bar's slanted ends. Through the triangles
    // it travels square to its own length, and it is exactly as long as their
    // long edges: it finishes flush on the first triangle and starts flush on the
    // second. All turns happen outside the mark.
    var start = at([594, 99.5]), turn1 = at([152, 99.5]), leave = at([84, 131.500]), enter = at([578, 428]), turn2 = at([510, 459]), end = at([68, 459]);
    line(start, turn1, 48, Math.PI + LEAN); var iA = out.length;
    bend(turn1, at([30, 100]), leave, Math.PI + LEAN, LEAN); var iD0 = out.length;
    line(leave, enter, 48, LEAN); var iD1 = out.length;
    bend(enter, at([640, 459]), turn2, LEAN, Math.PI + LEAN); var iC = out.length;
    line(turn2, end, 48, Math.PI + LEAN); out.push(end); angs.push(Math.PI + LEAN);

    var len = [0];
    for (var j = 1; j < out.length; j++) len[j] = len[j - 1] + Math.hypot(out[j][0] - out[j - 1][0], out[j][1] - out[j - 1][1]);
    return {
      pts: out, len: len, total: len[len.length - 1], blade: 185 * u, at: at, angs: angs, iA: iA, iD0: iD0, iD1: iD1, iC: iC,
      top: MARK.top.map(at), foldA: MARK.foldA.map(at), foldB: MARK.foldB.map(at), low: MARK.low.map(at)
    };
  }

  function polyPath(c, pts) {
    c.beginPath(); c.moveTo(pts[0][0], pts[0][1]);
    for (var i = 1; i < pts.length; i++) c.lineTo(pts[i][0], pts[i][1]);
    c.closePath();
  }

  function indexAt(path, s) {
    var target = s * path.total, l = path.len, lo = 0, hi = l.length - 1;
    while (lo < hi - 1) { var m = (lo + hi) >> 1; if (l[m] < target) lo = m; else hi = m; }
    return hi;
  }

  /* ----------------------------------------------------------- the hero -- */
  var stage = document.querySelector('[data-hero]');
  if (stage) (function () {
    var act = stage.closest('[data-sc-act]');
    var canvas = stage.querySelector('[data-film]');
    var near = stage.querySelector('[data-near]');
    var far = stage.querySelector('[data-far]');
    var scrim = stage.querySelector('[data-scrim]');
    var ctx = canvas.getContext('2d');
    var W = 0, H = 0, k = 1, film = null, path = null, beads = [], last = -1;
    var blade = document.createElement('canvas');
    var pointer = { x: 0, y: 0, tx: 0, ty: 0 };
    var fine = matchMedia('(hover: hover) and (pointer: fine)').matches && !reduce;

    function layout(force) {
      var cw = stage.clientWidth, ch = stage.clientHeight;
      // A phone's URL bar changes the height by a little: do not rebuild for that.
      if (!force && cw === W && Math.abs(ch - H) < 130) return;
      W = cw; H = ch;
      k = Math.min(window.devicePixelRatio || 1, W > 1100 ? 1.25 : 1.5);
      canvas.width = Math.round(W * k); canvas.height = Math.round(H * k);
      film = makeFilm(canvas.width, canvas.height, k);
      var copy = stage.querySelector('.hero__copy');
      path = buildPath(W, H, copy.offsetTop + copy.offsetHeight);
      var r = rng(11);
      beads = [];
      for (var i = 0; i < 72; i++) {
        // Water leaves from the free lower edges of the two bars.
        var upper = r() < .36, mx = upper ? 322 + r() * 220 : 21 + r() * 435, pos = path.at([mx, upper ? 167 : 527]);
        var from = upper ? 0 : path.iC, to = upper ? path.iA : path.pts.length - 1, n = from;
        while (n < to && path.pts[n][0] - SLOPE * (pos[1] - path.pts[n][1]) > pos[0]) n++;
        beads.push({ x: pos[0], y: pos[1], s: path.len[n] / path.total, fall: .12 + r() * r() * 1.1, size: .7 + r() * 1.25, drift: (r() - .5) * 6, wob: (r() - .5) * 5 });
      }
      makeBlade();
      // Push through the middle of a real pane, wherever the crop put it.
      var iw = 1599, ih = 1248, cover = Math.max(W / iw, H / ih), posX = W > 760 ? .5 : .71;
      var ox = (W - iw * cover) * posX + 715 * cover, oy = H - ih * cover + 935 * cover;
      near.style.transformOrigin = W <= 760 && H > W ? '65% 55%' : (ox / W * 100).toFixed(2) + '% ' + (oy / H * 100).toFixed(2) + '%';
      last = -1;
    }

    // The tool itself: stainless channel, black rubber, short handle. Drawn once.
    function makeBlade() {
      var L = path.blade * k, T = Math.max(13, path.blade * .1) * k;
      blade.width = Math.ceil(T * 3.8); blade.height = Math.ceil(L + 12 * k);
      var b = blade.getContext('2d'), cx = T * 1.1, top = 6 * k;
      b.clearRect(0, 0, blade.width, blade.height);
      var hw = T * .62;
      // channel
      var g = b.createLinearGradient(cx - T * .5, 0, cx + T * .55, 0);
      g.addColorStop(0, '#6f7c88'); g.addColorStop(.22, '#eef3f6'); g.addColorStop(.55, '#aab6c1'); g.addColorStop(1, '#58626d');
      b.fillStyle = g; b.fillRect(cx - T * .5, top, T * 1.05, L);
      // rubber, on the side that meets the wet glass
      b.fillStyle = '#10141b'; b.fillRect(cx - T * .86, top + 1, T * .38, L - 2);
      b.fillStyle = 'rgba(255,255,255,.28)'; b.fillRect(cx - T * .86, top + 1, Math.max(1, .8 * k), L - 2);
      // end caps
      b.fillStyle = '#39424c';
      b.fillRect(cx - T * .9, top - 3 * k, T * 1.45, 4 * k);
      b.fillRect(cx - T * .9, top + L - 1 * k, T * 1.45, 4 * k);
    }

    // How much of each part the blade has passed: everything behind its edge.
    function behind(c, head) {
      var P = path.pts, big = Math.max(W, H) * 3;
      function half(side) {
        return function () {
          var q = P[head], lx = -Math.sin(LEAN) * big, ly = Math.cos(LEAN) * big;
          var nx = Math.cos(LEAN) * big * side, ny = Math.sin(LEAN) * big * side;
          c.moveTo(q[0] + lx, q[1] + ly); c.lineTo(q[0] - lx, q[1] - ly); c.lineTo(q[0] - lx + nx, q[1] - ly + ny); c.lineTo(q[0] + lx + nx, q[1] + ly + ny); c.closePath();
        };
      }
      return [
        { polys: [path.top], on: head > 0, clip: head < path.iA ? half(1) : null },
        { polys: [path.foldA, path.foldB], on: head > path.iD0, clip: head < path.iD1 ? half(-1) : null },
        { polys: [path.low], on: head >= path.iC, clip: head < P.length - 1 ? half(1) : null }
      ];
    }

    function eachPart(parts, fn) {
      parts.forEach(function (part) {
        if (!part.on) return;
        ctx.save();
        if (part.clip) { ctx.beginPath(); part.clip(); ctx.clip(); }
        part.polys.forEach(function (poly) { fn(poly, part); });
        ctx.restore();
      });
    }

    // Timeline, in hero progress: s = how far along the S, grow = the stroke
    // widening over the rest of the pane, fade = the last film running off.
    function draw(p) {
      var s = .045 + .955 * smooth(range(p, 0, .46));   // the first pull is already on the glass when the page lands
      var grow = reduce ? 0 : Math.pow(range(p, .5, .66), 1.6);
      var fade = reduce ? 0 : range(p, .6, .68);
      var cleared = fade >= 1;
      canvas.style.visibility = cleared ? 'hidden' : 'visible';
      if (cleared) return;

      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.globalCompositeOperation = 'source-over';
      ctx.globalAlpha = 1;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(film, 0, 0);
      ctx.setTransform(k, 0, 0, k, 0, 0);

      var head = s > .0005 ? indexAt(path, s) : 0;
      if (head > 0) {
        var parts = behind(ctx, head);
        var width = grow * Math.max(W, H) * 1.3;
        ctx.lineJoin = 'miter'; ctx.miterLimit = 8; ctx.lineCap = 'butt';
        // The wet band at the edge of the clean glass: darker water first, then
        // the bright meniscus. When the S opens out it keeps its corners.
        ctx.globalCompositeOperation = 'source-atop';
        [[width + 22, 'rgba(26,44,70,.20)'], [width + 7, 'rgba(16,32,58,.22)'], [width + 2.4, 'rgba(255,255,255,.82)']].forEach(function (band) {
          ctx.strokeStyle = band[1]; ctx.lineWidth = band[0];
          eachPart(parts, function (poly) { polyPath(ctx, poly); ctx.stroke(); });
        });
        ctx.globalCompositeOperation = 'destination-out';
        ctx.fillStyle = ctx.strokeStyle = '#000'; ctx.lineWidth = width;
        eachPart(parts, function (poly) { polyPath(ctx, poly); ctx.fill(); if (width > 0) ctx.stroke(); });

        // Water left behind: beads at the lower edge that run down the film,
        // cutting a clean track through it as they go.
        ctx.lineCap = 'round';
        for (var b = 0; b < beads.length; b++) {
          var bd = beads[b];
          if (bd.s > s) continue;
          var age = clamp((s - bd.s) * 2.6 + grow, 0, 1);
          var run = age * bd.fall * H * .3;
          var x1 = bd.x + bd.drift * age, y1 = bd.y + run;
          ctx.globalCompositeOperation = 'destination-out';
          ctx.strokeStyle = 'rgba(0,0,0,.6)';
          ctx.lineWidth = bd.size * .8;
          ctx.beginPath(); ctx.moveTo(bd.x, bd.y); ctx.quadraticCurveTo(bd.x + bd.wob * age, bd.y + run * .55, x1, y1); ctx.stroke();
          ctx.globalCompositeOperation = 'source-over';
          ctx.fillStyle = 'rgba(240,247,252,' + (.7 * (1 - grow * 2.4 > 0 ? 1 - grow * 2.4 : 0)) + ')';
          ctx.beginPath(); ctx.ellipse(x1, y1, bd.size * .85, bd.size * 1.25, 0, 0, 6.3); ctx.fill();
        }
      }

      // The blade rides the head of the stroke and lifts off when the S is done.
      var lift = range(p, .46, .5);
      if (!reduce && s > 0 && lift < 1) {
        var q = path.pts[head];
        var ang = path.angs[head];
        ctx.globalCompositeOperation = 'source-over';
        ctx.globalAlpha = 1 - lift;
        ctx.save();
        ctx.translate(q[0], q[1]);
        ctx.rotate(ang);
        ctx.translate(lift * 40, -lift * 26);
        ctx.shadowColor = 'rgba(6,14,32,.5)'; ctx.shadowBlur = 16; ctx.shadowOffsetY = 7;
        var bw = blade.width / k, bh = blade.height / k;
        // Handle trails behind the direction of travel, channel sits on the edge.
        ctx.scale(-1, 1);
        ctx.drawImage(blade, -bw * .29, -bh / 2, bw, bh);
        ctx.restore();
        // The clamp and the pole: someone below is holding this.
        var ex = W * 1.04 + lift * 80, ey = H * 1.16 + lift * 80;
        var qx = q[0] + lift * 40, qy = q[1] - lift * 26;
        var pa = Math.atan2(ey - qy, ex - qx), pl = Math.hypot(ex - qx, ey - qy), pw = Math.max(9, path.blade * .055);
        ctx.save();
        ctx.translate(qx, qy); ctx.rotate(pa);
        ctx.shadowColor = 'rgba(6,14,32,.42)'; ctx.shadowBlur = 14; ctx.shadowOffsetY = 6;
        var pg = ctx.createLinearGradient(0, -pw / 2, 0, pw / 2);
        pg.addColorStop(0, '#31507f'); pg.addColorStop(.32, '#6d93c4'); pg.addColorStop(.62, '#17407f'); pg.addColorStop(1, '#0b1a4a');
        ctx.fillStyle = pg; ctx.fillRect(4, -pw / 2, pl, pw);
        ctx.shadowColor = 'transparent';
        ctx.fillStyle = '#10141b'; ctx.fillRect(0, -pw * .78, pw * 3.2, pw * 1.56);
        ctx.fillStyle = 'rgba(255,255,255,.22)'; ctx.fillRect(pw * .4, -pw * .78, pw * 2.4, 1);
        ctx.restore();
        ctx.globalAlpha = 1;
      }
      if (fade > 0) {
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        ctx.globalCompositeOperation = 'destination-out';
        ctx.fillStyle = 'rgba(0,0,0,' + fade + ')';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
      }
      ctx.globalCompositeOperation = 'source-over';
    }

    function planes(p) {
      // The S opens and the camera moves through it. The next section scrolls up over this.
      var through = smooth(range(p, .5, .9));
      var settle = smooth(range(p, 0, .5));
      var px = pointer.x, py = pointer.y;
      // Each plane has its own rate. Near moves most, the sky barely at all.
      near.style.transform = 'translate3d(' + (px * -14) + 'px,' + (py * -5) + 'px,0) scale(' + ((1.06 + settle * .045) * Math.pow(11, through)) + ')';
      near.style.opacity = 1 - (W <= 760 && H > W ? smooth(range(p, .54, .66)) : smooth(range(p, .68, .8)));
      far.style.transform = 'translate3d(' + (px * 5) + 'px,' + (py * 3 + settle * -14) + 'px,0) scale(' + (1.08 + through * .1) + ')';
      scrim.style.opacity = 1 - smooth(range(p, .46, .6));
      var cue = stage.querySelector('.hero__copy');
      cue.style.pointerEvents = p > .46 ? 'none' : '';
    }

    function progress() {
      var r = act.getBoundingClientRect();
      return clamp(-r.top / Math.max(r.height - innerHeight, 1), 0, 1);
    }

    var visible = true;
    new IntersectionObserver(function (e) { visible = e[0].isIntersecting; }, { rootMargin: '10% 0px' }).observe(act);

    function frame() {
      requestAnimationFrame(frame);
      if (!visible) return;
      var moved = false;
      if (fine) {
        pointer.x += (pointer.tx - pointer.x) * .07; pointer.y += (pointer.ty - pointer.y) * .07;
        if (Math.abs(pointer.tx - pointer.x) > .001 || Math.abs(pointer.ty - pointer.y) > .001) moved = true;
      }
      var p = reduce ? .47 : progress();
      if (Math.abs(p - last) < .0004 && !moved) return;
      var changed = Math.abs(p - last) >= .0004;
      if (changed) draw(p);
      planes(p);
      if (changed) stage.setAttribute('data-sc-verify-state', p.toFixed(3));
      last = p;
    }

    if (fine) addEventListener('pointermove', function (e) {
      pointer.tx = (e.clientX / innerWidth - .5) * 2; pointer.ty = (e.clientY / innerHeight - .5) * 2;
    }, { passive: true });
    var rt;
    addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(function () { layout(false); }, 160); });
    layout(true);
    frame();
  })();

  /* ------------------------------------------------- pinned lists: active item -- */
  // The film's three lines and the four steps work the same way: everything is
  // visible, the active item opens, and its rule fills as the visitor scrolls,
  // so there is always something on screen still to come.
  document.querySelectorAll('[data-steps]').forEach(function (how) {
    var items = how.querySelectorAll('.steps li'), imgs = how.querySelectorAll('.how__media img'), cur = 0;
    function tick() {
      var r = how.getBoundingClientRect();
      var p = clamp(-r.top / Math.max(r.height - innerHeight, 1), 0, 1);
      var at = p * items.length * .999, i = Math.min(items.length - 1, Math.floor(at));
      if (i !== cur) {
        items[cur].classList.remove('is-on');
        items[i].classList.add('is-on');
        if (imgs.length) { imgs[cur].classList.remove('is-on'); imgs[i].classList.add('is-on'); }
        cur = i;
        how.querySelector('[data-sc-stage]').setAttribute('data-sc-verify-state', 'step' + i);
      }
      items[i].style.setProperty('--fill', (at - i).toFixed(3));
    }
    addEventListener('scroll', tick, { passive: true });
    how.querySelectorAll('.steps button').forEach(function (btn, i) {
      btn.addEventListener('click', function () { jump(how, (i + .5) / items.length); });
    });
    if (imgs.length) new IntersectionObserver(function (e, o) {
      if (e[0].isIntersecting) { imgs.forEach(function (im) { im.loading = 'eager'; }); o.disconnect(); }
    }, { rootMargin: '100% 0px' }).observe(how);
    tick();
  });

  /* ------------- phones: the film arrives as a sheet, its corners square up as it docks -- */
  var sheet = document.querySelector('.peak__stage');
  if (sheet) (function () {
    var phone = matchMedia('(max-width: 760px), (max-height: 520px) and (orientation: landscape)'), act = sheet.closest('.peak');
    function dockSheet() {
      if (!phone.matches || reduce) { sheet.style.removeProperty('--sheet-r'); return; }
      sheet.style.setProperty('--sheet-r', (clamp(act.getBoundingClientRect().top / 90, 0, 1) * 22).toFixed(1) + 'px');
    }
    addEventListener('scroll', dockSheet, { passive: true });
    addEventListener('resize', dockSheet);
    dockSheet();
  })();

  /* ---------------------------- keyboard: focus never lands on something unseen -- */
  function jump(act, p) {
    var r = act.getBoundingClientRect(), top = r.top + scrollY;
    window.scrollTo(0, top + (act.offsetHeight - innerHeight) * p);
  }
  var heroAct = document.getElementById('glas'), workAct = document.getElementById('objekte');
  if (heroAct) heroAct.addEventListener('focusin', function () { if (scrollY > 40 && !reduce) jump(heroAct, 0); });
  if (workAct && !reduce && workAct.getAttribute('data-sc-act') === 'pan') workAct.addEventListener('focusin', function () { jump(workAct, 1); });
})();
