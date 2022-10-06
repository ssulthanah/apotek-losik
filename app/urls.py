from django.urls import path
from . import views

urlpatterns = [
    # path('', views.dashboard,name='obat'),
    path('obat', views.obat,name='obat'),
    path('addobat',views.addobat,name='addobat'),
    path('updateobat/<str:id>',views.updateobat,name='updateobat'),
    path('delete/<str:id>',views.deleteobat,name='deleteobat'),  
    path('penjualan', views.penjualan,name='penjualan'),
    path('addpenjualan',views.addpenjualan,name='addpenjualan'),
    path('updatepenjualan/<str:id>',views.updatepenjualan,name='updatepenjualan'),
    path('deletepenjualan/<str:id>',views.deletepenjualan,name='deletepenjualan'),
    path('supplier', views.supplier,name='supplier'),
    path('addsupplier', views.addsupplier,name='addsupplier'),
    path('updatesupplier/<str:id>',views.updatesupplier,name='updatesupplier'),
    path('deletesupplier/<str:id>',views.deletesupplier,name='deletesupplier'),
    path('pembelian', views.pembelian,name='pembelian'),    
    path('addpembelian', views.addpembelian,name='addpembelian'),
    path('updatepembelian/<str:id>',views.updatepembelian,name='updatepembelian'),
    path('deletepembelian/<str:id>',views.deletepembelian,name='deletepembelian'),
    path('adddetailpembelian/<str:id>', views.adddetailpembelian, name = 'adddetailpembelian'),
    path('adddetailpenjualan/<str:id>', views.adddetailpenjualan, name = 'adddetailpenjualan')
]