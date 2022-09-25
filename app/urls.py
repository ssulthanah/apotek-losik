from django.urls import path
from . import views

urlpatterns = [
    path('obat', views.obat,name='obat'),
    path('addobat',views.addobat,name='addobat')    
]