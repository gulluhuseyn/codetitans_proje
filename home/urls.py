from django.urls import path
from .views import *

app_name = "home"

urlpatterns = [
    path('destination_overview',destination_overview_view,name="destination_overview"),  
    path('destination_review',destination_review_view,name="destination_review"),  
    path('best_holiday',best_holiday_view,name="best_holiday"),  
]