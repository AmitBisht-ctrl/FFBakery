// change image on click
function imgSlider(receivedImg1,receivedimg2){
    document.querySelector('.img1').src = receivedImg1
    document.querySelector('.img2').src = receivedimg2
}

// change background color and button color
function changeBgColor(color,darkcolor){
    const bg = document.querySelectorAll('.bg');
    const btn = document.querySelector('.content .textBox a');
    for(let i=0; i < bg.length; i++){
        bg[i].style.background = color;
        // bg[i].style.transition = '2s ease';
    }

    btn.style.background = darkcolor;
    btn.style.boxShadow = '0 0 20px ' + darkcolor;

}
    // {% comment %} const slider = document.querySelector('.Slider');
    // slider.style.background = color
    // slider.style.transition = '2s ease'; {% endcomment %}

    // const btnShadow = document.querySelector('.content .textBox a');
