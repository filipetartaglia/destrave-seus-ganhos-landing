// scroll reveal
  const reveals = document.querySelectorAll('.reveal');
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if(e.isIntersecting){
        e.target.classList.add('is-visible');
        io.unobserve(e.target);
      }
    });
  }, {threshold:0.12});
  reveals.forEach(el => io.observe(el));

  // faq accordion
  document.querySelectorAll('.faq-item').forEach(item => {
    const q = item.querySelector('.faq-q');
    const a = item.querySelector('.faq-a');
    q.addEventListener('click', () => {
      const isOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item.open').forEach(o => {
        o.classList.remove('open');
        o.querySelector('.faq-a').style.maxHeight = null;
      });
      if(!isOpen){
        item.classList.add('open');
        a.style.maxHeight = a.scrollHeight + 'px';
      }
    });
  });

  // hero line draw-in
  const heroPath = document.getElementById('hero-path');
  if(heroPath){
    const len = heroPath.getTotalLength();
    heroPath.style.strokeDasharray = len;
    heroPath.style.strokeDashoffset = len;
    requestAnimationFrame(() => {
      heroPath.style.transition = 'stroke-dashoffset 2.2s ease';
      heroPath.style.strokeDashoffset = 0;
    });
  }

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // gráfico do platô: linha vermelha se desenha ao entrar na tela
  const plateauCard = document.getElementById('plateau-card');
  const plateauPath = document.getElementById('plateau-draw-path');
  if (plateauCard && plateauPath && !prefersReducedMotion) {
    const plen = plateauPath.getTotalLength();
    plateauPath.style.strokeDasharray = plen;
    plateauPath.style.strokeDashoffset = plen;

    const plateauObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          plateauPath.style.transition = 'stroke-dashoffset 1.4s cubic-bezier(.16,1,.3,1) .3s';
          plateauPath.style.strokeDashoffset = 0;
          plateauObserver.unobserve(plateauCard);
        }
      });
    }, { threshold: 0.4 });
    plateauObserver.observe(plateauCard);
  }

  // preço: contagem sobe até o valor final ao entrar na tela
  const priceTarget = document.getElementById('price-count-target');
  if (priceTarget && !prefersReducedMotion) {
    const finalValue = parseInt(priceTarget.dataset.target, 10);
    const priceObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const duration = 900;
          const start = performance.now();
          function tick(now) {
            const progress = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            const current = Math.round(eased * finalValue);
            priceTarget.textContent = 'R$' + current;
            if (progress < 1) {
              requestAnimationFrame(tick);
            } else {
              priceTarget.textContent = 'R$' + finalValue;
            }
          }
          requestAnimationFrame(tick);
          priceObserver.unobserve(priceTarget);
        }
      });
    }, { threshold: 0.5 });
    priceObserver.observe(priceTarget);
  }

  // header hide on scroll down, show on scroll up
  const header = document.querySelector('header');
  let lastScrollY = window.scrollY;
  const scrollThreshold = 80;

  window.addEventListener('scroll', () => {
    const currentScrollY = window.scrollY;

    header.style.borderBottomColor = currentScrollY > 40 ? 'var(--border-bright)' : 'var(--border)';

    if (currentScrollY <= scrollThreshold) {
      header.classList.remove('header-hidden');
    } else if (currentScrollY > lastScrollY) {
      header.classList.add('header-hidden');
    } else if (currentScrollY < lastScrollY) {
      header.classList.remove('header-hidden');
    }

    lastScrollY = currentScrollY;
  });

  // "Descobrir Como Funciona" -> rola até o VSL e inicia o vídeo
  const descobrirBtn = document.getElementById('descobrir-btn');
  const vslIframe = document.getElementById('vsl-iframe');
  const vslSection = document.getElementById('vsl');

  if (descobrirBtn && vslIframe && vslSection) {
    descobrirBtn.addEventListener('click', (e) => {
      e.preventDefault();
      vslSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      if (window.vslVimeoPlayer) {
        window.vslVimeoPlayer.play();
      }
    });
  }

  // ---------- Meta Pixel: tracking de eventos ----------
  function trackPixel(eventName, params) {
    if (typeof fbq === 'function') {
      fbq('trackCustom', eventName, params || {});
    }
  }

  // Clique nos CTAs de checkout (Hotmart)
  document.querySelectorAll('a[href*="pay.hotmart.com"]').forEach((btn, index) => {
    btn.addEventListener('click', () => {
      const location = btn.closest('section')?.id || btn.closest('div[class]')?.className.split(' ')[0] || `cta-${index}`;
      if (typeof fbq === 'function') {
        fbq('track', 'InitiateCheckout', { content_name: 'Destrave Seus Ganhos', cta_location: location });
      }
    });
  });

  // Clique no botão "Descobrir Como Funciona" (intenção de assistir VSL)
  if (descobrirBtn) {
    descobrirBtn.addEventListener('click', () => {
      trackPixel('VSL_Click', { source: 'hero_button' });
    });
  }

  // Play real do vídeo VSL via Vimeo Player API
  (function loadVimeoAPI() {
    if (!vslIframe) return;
    let vslPlayTracked = false;

    const tag = document.createElement('script');
    tag.src = 'https://player.vimeo.com/api/player.js';
    tag.onload = function () {
      const player = new Vimeo.Player(vslIframe);
      window.vslVimeoPlayer = player;
      player.on('play', function () {
        if (!vslPlayTracked) {
          vslPlayTracked = true;
          trackPixel('VSL_Play', { video: 'destrave-seus-ganhos' });
        }
      });
    };
    document.head.appendChild(tag);
  })();

  // Profundidade de scroll (25% / 50% / 75% / 100%)
  (function scrollDepthTracking() {
    const milestones = [25, 50, 75, 100];
    const reached = new Set();

    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      if (docHeight <= 0) return;
      const percent = Math.round((scrollTop / docHeight) * 100);

      milestones.forEach((m) => {
        if (percent >= m && !reached.has(m)) {
          reached.add(m);
          trackPixel('ScrollDepth', { percent: m });
        }
      });
    });
  })();
