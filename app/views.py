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
    


