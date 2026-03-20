// Typing animation for hero
const texts = [
  'gatinho fofo com chapéu...',
  'leão com juba grande...',
  'princesa no castelo...',
  'robô brincando no parque...',
  'unicórnio voando nas nuvens...',
  'dinossauro sorridente...'
];

let textIdx = 0;
let charIdx = 0;
let isDeleting = false;
const typingEl = document.getElementById('typingText');

function typeText() {
  if (!typingEl) return;
  const current = texts[textIdx];
  
  if (!isDeleting) {
    typingEl.textContent = current.substring(0, charIdx + 1);
    charIdx++;
    if (charIdx === current.length) {
      isDeleting = true;
      setTimeout(typeText, 2000);
      return;
    }
  } else {
    typingEl.textContent = current.substring(0, charIdx - 1);
    charIdx--;
    if (charIdx === 0) {
      isDeleting = false;
      textIdx = (textIdx + 1) % texts.length;
    }
  }
  setTimeout(typeText, isDeleting ? 50 : 80);
}

typeText();

// Scroll animations
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.feature-card, .step, .plan-card').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(20px)';
  el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  observer.observe(el);
});
