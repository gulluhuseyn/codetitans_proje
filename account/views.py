from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages
# Create your views here.
from django.core.mail import send_mail

def register_view(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form":form,
        }
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        
        newUser = User(email=email,password=password)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        
        subject = 'About Registration'
        message = f'Hi ,You has been registered successfully on website.'
        email_from = 'travojourney@gmail.com'
        rec_list = [email,]
        response = send_mail(
            subject,
            message,
            email_from,
            rec_list,
            fail_silently=False
        )
        print("UYFRUYYUBTYUTBYUTUYBGUN", response)
        
        messages.success(request, 'User has been sucessfully registered')

        return redirect("home")
    
    return render(request,"register.html",context)

def login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form,
    }
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = authenticate(email=email,password=password)

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