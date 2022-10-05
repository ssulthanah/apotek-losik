from datetime import datetime
from django.shortcuts import render, redirect
from . import models
from django.forms import inlineformset_factory

# Create your views here.

# def dashboard(request):
#     dataobat = models.obat.objects.filter ()

def obat(request):
    allobatobj = models.obat.objects.all()
    # getobatobj = models.obat.objects.get(idobat=5)
    
    return render (request, 'obat.html',{
    'allobatobj' : allobatobj, 
    # 'getobatobj' : getobatobj   
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

        models.obat(
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
            'obatobj' : obatobj
        })
        
    else:
        obatobj.jenisobat = request.POST['jenisobat']
        obatobj.namaobat = request.POST['namaobat']
        obatobj.jumlahstock = request.POST['jumlahstock']
        obatobj.hargabeli = request.POST['hargabeli']
        obatobj.hargajual = request.POST['hargajual']
        obatobj.satuan = request.POST['satuan']
        obatobj.save()
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

        models.penjualan(
            namaapoteker = namaapoteker,
            namapelanggan = namapelanggan,
            tanggaltransaksi = tanggaltransaksi,
        ).save()
        return redirect('penjualan')

def updatepenjualan(request,id):
    penjualanobj = models.penjualan.objects.get(idpenjualan=id)
    if request.method == "GET":
        tanggal = datetime.strftime(penjualanobj.tanggaltransaksi, '%d-%m-%Y')
        return render(request, 'updatepenjualan.html', {
            'penjualanobj' : penjualanobj,
            'tanggaltransaksi' : tanggal
        })
        
    else:
        penjualanobj.namaapoteker = request.POST['namaapoteker']
        penjualanobj.namapelanggan = request.POST['namapelanggan']
        penjualanobj.tanggaltransaksi = request.POST['tanggaltransaksi']
        penjualanobj.save()
        return redirect('penjualan')

def deletepenjualan(request,id):
    penjualanobj = models.penjualan.objects.get(idpenjualan=id)
    penjualanobj.delete()
    return redirect('penjualan')

def supplier(request):
    allsupplierobj = models.supplier.objects.all()

    return render (request, 'supplier.html', {
        'allsupplierobj': allsupplierobj,
    })

def pembelian(request):
    # pembelian = models.pembelian.get(id = pk)
    allpembelianobj = models.pembelian.objects.all()
    return render (request, 'pembelian.html', {
        'allpembelianobj': allpembelianobj,

    })

def addpembelian (request) :
    if request.method == "GET" :   
        allsupplierobj = models.supplier.objects.all()
        return render(request, 'addpembelian.html', {
            'datasupplier' : allsupplierobj
        })
    if request.method == "POST":
        idsupplier = request.POST['idsupplier']
        getsupplierobj = models.supplier.objects.get(idsupplier= idsupplier)
        namaapoteker = request.POST['namaapoteker']
        tanggalpembelian = request.POST['tanggalpembelian']

        newpembelian = models.pembelian(
            idsupplier = getsupplierobj,
            namaapoteker = namaapoteker,
            tanggalpembelian = tanggalpembelian,
        )
        newpembelian.save()
        return redirect('pembelian')

def adddetailpembelian(request, id):
    OrderFormSet = inlineformset_factory(models.pembelian, models.detailpembelian, fields = ('idobat', 'jumlahobatdibeli'))
    pembelian = models.pembelian.objects.get(idpembelian = id)
    formset = OrderFormSet (instance = pembelian)
    if request.method == 'POST':
        formset = OrderFormSet (request.POST, instance = pembelian)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset' : formset}
    return render (request, 'adddetailpembelian.html', context)
    
def updatepembelian(request,id):
    pembelianobj = models.pembelian.objects.get(idpembelian=id)
    if request.method == "GET":
        allsupplierobj = models.supplier.objects.all()
        tanggalbeliobj = datetime.strftime(pembelianobj.tanggalpembelian, '%Y-%m-%d')
        return render(request, 'updatepembelian.html', {
            'pembelianobj' : pembelianobj,
            'datasupplier' : allsupplierobj,
            'tanggalbeliobj' : tanggalbeliobj
        })
        
    else:
        pembelianobj.namaapoteker = request.POST['namaapoteker']
        pembelianobj.tanggalpembelian = request.POST['tanggalpembelian']
        pembelianobj.save()
        return redirect('pembelian')

def deletepembelian(request, id):
    pembelianobj = models.pembelian.objects.get(idpembelian=id)
    pembelianobj.delete()
    return redirect('pembelian')