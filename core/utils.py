# import pyotp
from datetime import datetime,timedelta


# # otp code generating here
# def send_otp(request):
#     totp=pyotp.TOTP(pyotp.random_base32(),interval=60)
#     otp=totp.now()
#     request.session["otp_secret_key"]=totp.secret
#     valid_date=datetime.now() + timedelta(minutes=1)
#     request.session['otp_valid_date']=str(valid_date)

#     print(F'your otp:{otp}')


# import pyotp
# from django.core.mail import send_mail
# from django.conf import settings

# def send_otp(request, email):
#     # OTP generator
#     otp = pyotp.TOTP(settings.SECRET_KEY).now()
    
#     # OTP və e-poçtu sessiyada saxlayırıq
#     request.session["otp"] = otp
#     request.session["user_email"] = email
    
#     # OTP-ni e-poçt vasitəsilə göndərin
#     send_mail(
#         'Sizin OTP Kodu',
#         f'Sizin OTP kodunuz {otp}',
#         settings.DEFAULT_FROM_EMAIL,
#         [email],
#         fail_silently=False,
#     )

# def verify_otp(email, otp):
#     # Sessiyada saxlanılan OTP ilə müqayisə edirik
#     return otp == request.session.get("otp")
