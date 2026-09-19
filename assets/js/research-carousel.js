// Homepage carousel. Interval is in ms; pauses while the mouse is over it.
const INTERVAL_MS = 6000;

document.addEventListener("DOMContentLoaded", function () {
  const carousel = document.getElementById("research-carousel");
  if (!carousel) return;
  const slides = carousel.querySelectorAll(".jb-slide");
  const dots = carousel.querySelectorAll(".jb-dot");
  if (!slides.length) return;

  let current = 0, timer = null;

  function show(i) {
    current = (i + slides.length) % slides.length;
    slides.forEach((s, k) => s.classList.toggle("active", k === current));
    dots.forEach((d, k) => d.classList.toggle("active", k === current));
  }
  function start() { stop(); timer = setInterval(() => show(current + 1), INTERVAL_MS); }
  function stop() { if (timer) { clearInterval(timer); timer = null; } }

  dots.forEach((d, k) => d.addEventListener("click", () => { show(k); start(); }));
  carousel.querySelector(".jb-prev")?.addEventListener("click", () => { show(current - 1); start(); });
  carousel.querySelector(".jb-next")?.addEventListener("click", () => { show(current + 1); start(); });
  carousel.addEventListener("mouseenter", stop);
  carousel.addEventListener("mouseleave", start);

  show(0);
  start();
});
