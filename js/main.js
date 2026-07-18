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
      vslIframe.src = 'https://www.youtube.com/embed/oW7vzJii55k?rel=0&modestbranding=1&enablejsapi=1&autoplay=1';
      vslSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
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

  // Play real do vídeo VSL via YouTube IFrame API
  (function loadYouTubeAPI() {
    if (!vslIframe) return;
    let vslPlayTracked = false;

    const tag = document.createElement('script');
    tag.src = 'https://www.youtube.com/iframe_api';
    document.head.appendChild(tag);

    window.onYouTubeIframeAPIReady = function () {
      new YT.Player('vsl-iframe', {
        events: {
          onStateChange: function (event) {
            if (event.data === YT.PlayerState.PLAYING && !vslPlayTracked) {
              vslPlayTracked = true;
              trackPixel('VSL_Play', { video: 'destrave-seus-ganhos' });
            }
          }
        }
      });
    };
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
