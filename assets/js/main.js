(function () {
  var html = document.documentElement;
  var lang = html.getAttribute('lang') === 'ko' ? 'ko' : 'en';

  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* ---- Language: Wix sends Korean-language browsers from / to /ko unless a language was chosen ---- */
  if (lang === 'en' && !store('site-lang') && /^ko/i.test(navigator.language || '')) {
    var alt = document.querySelector('link[rel="alternate"][hreflang="ko-kr"]');
    if (alt) { location.replace(alt.getAttribute('href')); return; }
  }

  var sel = document.querySelector('.lang');
  if (sel) {
    var btn = sel.querySelector('.lang-btn');
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = sel.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
    document.addEventListener('click', function () { sel.classList.remove('open'); btn.setAttribute('aria-expanded', false); });
    sel.querySelectorAll('.lang-list a').forEach(function (a) {
      a.addEventListener('click', function () { store('site-lang', a.getAttribute('data-lang')); });
    });
  }

  /* ---- Career Album: Wix Pro Gallery masonry (2 columns, 20px gap, 200px text area, shortest column first) ---- */
  var gallery = document.querySelector('.gallery');
  if (!gallery) return;
  var items = Array.prototype.slice.call(gallery.querySelectorAll('.g-item'));
  var GAP = 20, INFO = 200;

  function layout() {
    if (window.innerWidth < 1000) { gallery.style.height = ''; items.forEach(function (it) { it.style.cssText = ''; it.querySelector('.g-img').style.height = ''; }); return; }
    var W = gallery.clientWidth, colW = (W - GAP) / 2, cols = [0, 0];
    items.forEach(function (it) {
      var ratio = +it.getAttribute('data-ratio');
      var c = cols[1] < cols[0] ? 1 : 0;
      var h = colW * ratio;
      it.style.left = (c * (colW + GAP)) + 'px';
      it.style.top = cols[c] + 'px';
      it.style.width = colW + 'px';
      it.querySelector('.g-img').style.height = h + 'px';
      cols[c] += h + INFO + GAP;
    });
    gallery.style.height = (Math.max(cols[0], cols[1]) - GAP) + 'px';
  }
  layout();
  window.addEventListener('resize', layout);

  /* ---- Lightbox ---- */
  var lb = document.querySelector('.lb'), lbImg = lb.querySelector('.lb-stage img'), lbCap = lb.querySelector('.lb-cap');
  var prev = lb.querySelector('.lb-prev'), next = lb.querySelector('.lb-next'), idx = 0;

  function show(i) {
    idx = i;
    var it = items[i];
    lbImg.src = it.querySelector('img').getAttribute('src');
    lbCap.textContent = it.querySelector('.g-info').textContent;
    prev.hidden = i === 0;
    next.hidden = i === items.length - 1;
  }
  function open(i) { show(i); lb.classList.add('open'); document.body.style.overflow = 'hidden'; }
  function close() { lb.classList.remove('open'); document.body.style.overflow = ''; }

  items.forEach(function (it, i) { it.addEventListener('click', function () { open(i); }); });
  lb.querySelector('.lb-close').addEventListener('click', close);
  prev.addEventListener('click', function () { if (idx > 0) show(idx - 1); });
  next.addEventListener('click', function () { if (idx < items.length - 1) show(idx + 1); });
  document.addEventListener('keydown', function (e) {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft' && idx > 0) show(idx - 1);
    if (e.key === 'ArrowRight' && idx < items.length - 1) show(idx + 1);
  });
})();
