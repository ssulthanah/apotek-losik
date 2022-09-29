from datetime import datetime
import re
from django.shortcuts import render, redirect
from . import models

# Create your views here.

def obat(request):
    allobatobj = models.obat.objects.all()
    
    return render (request, 'obat.html',{
    'allobatobj' : allobatobj,    
    })
    
def addobat (request) :
    if request.method == "GET" :
        return render(request, 'addobat.html')
    else:
        jenisobat = request.POST['jenisobat']
        namaobat = request.POST['namaobat']
        jumlahstock = request.POST['jumlahstock']
        hargabeli = request.POST['hargabeli']
        hargajual = request.POST['hargajual']
        satuan = request.POST['satuan']

        newobat = models.obat(
            jenisobat = jenisobat,
            namaobat = namaobat,
            jumlahstock = jumlahstock,
            hargabeli = hargabeli,
            hargajual = hargajual,
            satuan = satuan,
        ).save()
        return redirect('obat')

def updateobat(request,id):
    obatobj = models.obat.objects.get(idobat=id)
    if request.method == "GET":
        return render(request, 'updateobat.html', {
            'obat' : obatobj
        })
        
    else:
        obatobj.namaobat = request.POST['namaobat']
        obatobj.jenisobat = request.POST['jenisobat']
        obatobj.jumlahstock = request.POST['jumlahstock']
        obatobj.hargabeli = request.POST['hargabeli']
        obatobj.hargajual = request.POST['hargajual']
        obatobj.satuan = request.POST['satuan']
        obatobj.save
        return redirect('obat')

def deleteobat(request, id):
    obatobj = models.obat.objects.get(idobat=id)
    obatobj.delete()
    return redirect('obat')
    
def penjualan (request):
    allpenjualanobj = models.penjualan.objects.all()

    return render (request, 'penjualan.html', {
        'allpenjualanobj': allpenjualanobj,
    })

def addpenjualan (request) :
    if request.method == "GET" :
        return render(request, 'addpenjualan.html')
    else:
        namaapoteker = request.POST['namaapoteker']
        namapelanggan = request.POST['namapelanggan']
        tanggaltransaksi = request.POST['tanggaltransaksi']

        newobat = models.penjualan(
            namaapoteker = namaapoteker,
            namapelanggan = namapelanggan,
            tanggaltransaksi = tanggaltransaksi,
        ).save()
        return redirect('penjualan')

def updatepenjualan(request,id):
    penjualanobj = models.penjualan.objects.get(idpenjualan=id)
    if request.method == "GET":
        return render(request, 'updatepenjualan.html', {
            'penjualan' : penjualanobj
        })
        
    else:
        penjualanobj.namaapoteker = request.POST['namaapoteker']
        penjualanobj.namapelanggan = request.POST['namapelanggan']
        penjualanobj.tanggaltransaksi = request.POST['tanggaltransaksi']
        penjualanobj.hargabeli = request.POST['hargabeli']
        penjualanobj.save
        return redirect('penjualan')

def deletepenjualan(request, id):
    penjualanobj = models.penjualan.objects.get(idpenjualan=id)
    penjualanobj.delete()
    return redirect('obat')

