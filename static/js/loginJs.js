const signinBtn = document.querySelector('.signinBtn');
const signupBtn = document.querySelector('.signupBtn');
const formBx = document.querySelector('.formBx');
const body = document.querySelector('.body');
const bg = document.querySelectorAll('.bg');
var failure = document.querySelector('.message_failure')
var closeFailureMsg = document.querySelector('.close')

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

closeFailureMsg.onclick = function(){
    failure.classList.remove('show')
    failure.classList.add('hide')
    }

    // closeFailureMsg.addEventListener('click',function(){
    //     console.log(failure.classList)
    //     failure.classList.remove('show')
    //     failure.classList.add('hide')
    // })