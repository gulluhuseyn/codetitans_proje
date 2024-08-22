from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages
# Create your views here.
def register_view(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form":form,
        }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        
        login(request,newUser)
        messages.warning(request,"Siz uğurla qeydiyyatdan keçdiniz...")

        return redirect("home")
    
    return render(request,"register.html",context)


def login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username,password=password)

        if user is None:
            return render(request,"login.html")
        
        login(request,user)
        messages.success(request,f"Xoş gəlmisiniz {request.user.username}")
        
        return redirect("home")

    return render(request,"login.html",context)

def forgot_password_view(request):
    return render(request,"forgot_password.html")


def enter_otp_view(request):
    return render(request,"enter_otp.html")

def login_success_view(request):
    return render(request,"login_success.html")