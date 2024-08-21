"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import *
urlpatterns = [
    path('',home_view,name="home"),
    path('about_us',about_us_view,name="about_us"),
    path('services',services_view,name="services"),
    path('destinations',destinations_view,name="destinations"),
    path('blog',blog_view,name="blog"),
    path('contact_us',contact_us_view,name="contact_us"),
    path('account/',include("account.urls")),
    path('admin/', admin.site.urls),   
]
