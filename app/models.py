from tkinter import CASCADE
from django.db import models

# Create your models here.
class obat(models.Model):
    idobat = models.CharField(max_length=5, primary_key=True)
    jenisobat = models.CharField(max_length=50)
    namaobat = models.CharField(max_length=10)
    jumlahstock = models.IntegerField()
    hargabeli = models.IntegerField()
    hargajual = models.IntegerField()
    satuan = models.CharField()

    def __str__(self):
        return str(self.namaobat)

class penjualan(models.Model):
    idpenjualan = models.CharField(max_length=5, primary_key=True)
    namaapoteker = models.CharField(max_length=50)
    namapelanggan = models.CharField(max_length=50)
    tanggaltransaksi = models.DateField()

    def __str__(self):
        return str(self.namapelanggan)

class supplier(models.Model):
    idsupplier = models.CharField(max_length=5, primary_key=True)
    namasupplier = models.CharField(max_length=50)
    alamat = models.CharField(max_length=50)
    nohp = models.IntegerField()

    def __str__(self):
        return str(self.namasupplier)

class pembelian(models.Model):
    idpembelian = models.CharField(max_length=5, primary_key=True)
    idsupplier = models.ForeignKey(supplier, on_delete=models.CASCADE)
    namaapoteker = models.CharField(max_length=50)
    tanggalpembelian = models.DateField()

    def __str__(self):
        return str(self.idsupplier)

class detailpenjualan(models.Model):
    iddetailpenjualan = models.AutoField(max_length=5, primary_key=True)
    idpenjualan = models.ForeignKey(penjualan, on_delete=models.CASCADE)
    idobat = models.ForeignKey(obat, on_delete=models.CASCADE)
    jumlahobatterjual = models.IntegerField()

    def __str__(self):
        return str(self.idpenjualan)

class detailpembelian(models.Model):
    iddetailpembelian = models.AutoField(max_length=5, primary_key=True)
    idpembelian = models.ForeignKey(pembelian, on_delete=models.CASCADE)
    idobat = models.ForeignKey(obat, on_delete=models.CASCADE)
    jumlahobatdibeli = models.IntegerField()

    def __str__(self):
        return str(self.idpembelian)
