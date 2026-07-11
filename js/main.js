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
