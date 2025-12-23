console.log("Medical Clinic Django Site Loaded");

const slides = document.querySelector(".slides");
const totalSlides = document.querySelectorAll(".slide").length;
let currentSlide = 0;

function autoSlide() {
    currentSlide++;

    if (currentSlide >= totalSlides) {
        currentSlide = 0;
    }

    slides.style.transform = `translateX(-${currentSlide * 100}%)`;
}

setInterval(autoSlide, 5000);

