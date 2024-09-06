# from django.shortcuts import render,redirect
# from .forms import RegisterForm,LoginForm
# from django.contrib.auth.models import User
# from django.contrib.auth import login,authenticate
# from django.contrib import messages
# # Create your views here.
# # from django.core.mail import send_mail

# def register_view(request):
#     form = RegisterForm(request.POST or None)
#     context = {
#         "form":form,
#         }
#     if request.method == "POST":
#         if form.is_valid():
#             email = form.cleaned_data.get("email")
#             password = form.cleaned_data.get("password")

#             newUser = User(email = email)
#             newUser.set_password(password)
            
#             newUser.save()
#             login(request,newUser)
            
#             messages.success(request, 'User has been sucessfully registered')

#             return redirect("home")
    
#     return render(request,"register.html",context)

# def login_view(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         "form":form,
#     }
#     if form.is_valid():
#         email = form.cleaned_data.get("email")
#         password = form.cleaned_data.get("password")

#         user = authenticate(email=email,password=password)

#         if user is None:
#             return render(request,"login.html")
        
#         login(request,user)
#         messages.success(request,f"Xoş gəlmisiniz {request.user.username}")
        
#         return redirect("home")

#     return render(request,"login.html",context)
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest
from .forms import SignUp
from django.contrib.auth import login
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import messages
from core.utils import send_otp
from datetime import datetime
import pyotp



from django.contrib.auth import authenticate,login
from .forms import Log_In


# Create your views here.
def register_view(request):
    form=SignUp(request.POST or None)


    if form.is_valid():
        email=    form.cleaned_data.get("email")
        users=User.objects.filter(email=email).exists()
        if users:
            messages.error(request," Email Is Taken" )
            return redirect("SignUp")

        firstname=form.cleaned_data.get("firstname")
        lastname= form.cleaned_data.get("lastname")
        
        password= form.cleaned_data.get("password")
        

        newUser=User.objects.create_user(username=firstname,first_name=firstname,last_name=lastname, email=email, password=password)
        newUser.username=firstname
        newUser.first_name=firstname
        newUser.last_name= lastname
        newUser.email=email
        newUser.set_password=password
        newUser.save()
        login(request, newUser)
        return redirect("home")
    
    context={"form":form}
    return render(request,"register.html",context)

def login_view(request):
   form=Log_In(request.POST or None)
   context={"form":form}
   if form.is_valid():
      email=    form.cleaned_data.get("email")  
      password= form.cleaned_data.get("password")
      user=authenticate(email=email,password =password)
      if user is None:
         messages.error(request,"Wrong Email or Password" )
         return render(request,"login.html")
      
      request.session["user_email"]=email
      send_otp(request)
      return redirect("enter_otp")
      
   return render(request,"login.html", context)

def enter_otp_view(request):
   if request.method=="POST":
      otp=request.POST['otp']

      otp_secret_key=request.session['otp_secret_key']
      otp_valid_until=request.session['otp_valid_date']
      if otp_secret_key and otp_valid_until is not None:
         valid_until=datetime.fromisoformat(otp_valid_until)
         if valid_until>datetime.now():
            totp=pyotp.TOTP(otp_secret_key, interval=60)
            if totp.verify(otp):
                email=request.session["user_email"]
                user=get_object_or_404(User,email=email)
                login(request, user)
                del request.session["otp_secret_key"]
                del request.session["otp_valid_date"]
                return redirect('home')

   return render(request, "enter_otp.html")

# def Log_Out_Page(request):
#    logout(request)
#    return redirect('Login')

def forgot_password_view(request):
   if request.method=="POST":
      email=request.POST["email"]
      users=User.objects.filter(email=email).exists()
      if users:
         password=User.objects.filter(email=email).values_list('password')
         print(f' your passowrd{password}')
         messages.success(request,f'Your Password:{ password}' )
      else:
         messages.error(request,'Wrong Email' )

   return render(request,"forgot_password.html")
# def forgot_password_view(request):
#     return render(request,"forgot_password.html")


# def enter_otp_view(request):
#     return render(request,"enter_otp.html")

def login_success_view(request):
    return render(request,"login_success.html")