from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,"home.html")

def about_us_view(request):
    return render(request,"about_us.html")

def services_view(request):
    return render(request,"services.html")

def destinations_view(request):
    return render(request,"destinations.html")

def blog_view(request):
    return render(request,"blog.html")

def blog_detail_view(request):
    return render(request,"blog_detail.html")

def contact_us_view(request):
    return render(request,"contact_us.html")