from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path('register',register_view,name="register"),  
    path('login',login_view,name="login"),  
    path('forgot_password',forgot_password_view,name="forgot_password"),   
    path('enter_otp',enter_otp_view,name="enter_otp"),    
]