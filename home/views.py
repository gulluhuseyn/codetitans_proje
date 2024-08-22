from django.shortcuts import render

# Create your views here.
def destination_overview_view(request):
    return render(request,"destination_overview.html")

def destination_review_view(request):
    return render(request,"destination_review.html")