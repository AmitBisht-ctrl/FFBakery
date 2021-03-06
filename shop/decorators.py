from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

def login_must(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request,'You need to be <span>logged in</span>, to access this feature.')
            return redirect('home')

    return wrapper_func

def already_logged(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request,'You are already <span>logged in</span>.')
            return redirect('home')
        
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
