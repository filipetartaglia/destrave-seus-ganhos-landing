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

  // header shrink on scroll (subtle)
  const header = document.querySelector('header');
  window.addEventListener('scroll', () => {
    if(window.scrollY > 40){
      header.style.borderBottomColor = 'var(--border-bright)';
    } else {
      header.style.borderBottomColor = 'var(--border)';
    }
  });
