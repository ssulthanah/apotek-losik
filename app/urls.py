from django.urls import path
from . import views

urlpatterns = [
    path('obat', views.obat,name='obat'),
    path('addobat',views.addobat,name='addobat'),
    path('update/<str:id>',views.updateobat,name='updateobat'),
    path('delete/<str:id>',views.deleteobat,name='deleteobat')  
]