from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.obat)
admin.site.register(models.penjualan)
admin.site.register(models.supplier)
admin.site.register(models.pembelian)
admin.site.register(models.detailpenjualan)
admin.site.register(models.detailpembelian)