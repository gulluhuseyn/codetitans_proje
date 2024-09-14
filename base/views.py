from django.shortcuts import render, redirect
from .models import BlogComment
from .forms import BlogCommentForm

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
    blog_comments = BlogComment.objects.all()
    
    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.email = request.user
            comment.save()
        
            return redirect('blog_detail') 
    else:
        form = BlogCommentForm()

    context = {
        'form': form,
        'blog_comments': blog_comments
    }
    return render(request,"blog_detail.html",context)


def contact_us_view(request):
    return render(request,"contact_us.html")