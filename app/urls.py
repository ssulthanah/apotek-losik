from django.urls import path
from . import views

urlpatterns = [
    path('obat', views.obat,name='obat'),
    path('addobat',views.addobat,name='addobat'),
    path('updateobat/<str:id>',views.updateobat,name='updateobat'),
    path('delete/<str:id>',views.deleteobat,name='deleteobat'),  
    path('penjualan', views.penjualan,name='penjualan'),
    path('addpenjualan',views.addpenjualan,name='addobat'),
    # path('updatepenjualan/<str:id>',views.updateobat,name='updateobat'),
    # path('deletepenjualan/<str:id>',views.deleteobat,name='deleteobat')
]