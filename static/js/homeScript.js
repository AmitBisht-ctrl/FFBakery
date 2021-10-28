// change image on click
function changeImg(receivedImg){
    document.querySelector('.imgBox img').src = receivedImg
}

// change background color and button color
function changeBgColor(color,darkcolor){
    const bg = document.querySelectorAll('.bg');
    const btn = document.querySelector('.content .textBox a');
    for(let i=0; i < bg.length; i++){
        bg[i].style.background = color;
        bg[i].style.transition = '1s ease';
    }

    btn.style.background = darkcolor;
    btn.style.boxShadow = '0 0 20px ' + darkcolor;

    const slider = document.querySelector('.categoryIcons');
    slider.style.background = color
    slider.style.transition = '1s ease';
}

// add active class in selected thumbnails
let el = document.querySelectorAll('.thumb li');
for (let i = 0; i < el.length; i++){
    el[i].onclick = function(){
        var c = 0;
        while(c < el.length){
            el[c++].className = 'check';
        }
    el[i].className = 'check active'
    }
}


// Swiper.js here
var swiper = new Swiper(".mySwiper", {
    effect: "coverflow",
    grabCursor: true,
    keyboard: true,
    // mousewheel: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 5,
        modifier: 1,
        slideShadows: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});
