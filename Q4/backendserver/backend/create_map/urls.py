from django.urls import path
from . import views

urlpatterns=[
    path('calculatePrice/',views.calculate_price),
   

]
