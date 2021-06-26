const signinBtn = document.querySelector('.signinBtn');
const signupBtn = document.querySelector('.signupBtn');
const formBx = document.querySelector('.formBx');
const body = document.querySelector('.body');
const bg = document.querySelectorAll('.bg');


signupBtn.onclick = function(){
    formBx.classList.add('active');
    body.classList.add('active');
    for(let i=0; i < bg.length; i++){
        bg[i].style.background = '#f464f4';
    }
}

signinBtn.onclick = function(){
    formBx.classList.remove('active');
    body.classList.remove('active');
    for(let i=0; i < bg.length; i++){
        bg[i].style.background = '#03a9f4';
    }
}
