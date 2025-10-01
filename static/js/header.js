document.addEventListener('DOMContentLoaded', function () {
    const header = document.querySelector('.landing-header');
    if (!header) return; // só roda na landing
  
    const threshold = 50; // px que o usuário precisa rolar antes de trocar a cor
  
    function onScroll() {
      if (window.scrollY > threshold) header.classList.add('scrolled');
      else header.classList.remove('scrolled');
    }
  
    // roda uma vez ao carregar (útil se a URL vier com âncora)
    onScroll();
  
    // escuta o scroll
    window.addEventListener('scroll', onScroll, { passive: true });
  });