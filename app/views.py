from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def Insert_Topic(request):
    if request.method=='POST':
        to=request.POST['tn']
        tlo=Topic.objects.get_or_create(Topic_name=to)[0]
        tlo.save()
        return HttpResponse("Data Inserted successfully!!!")

    return render(request,'Insert_Topic.html')

def Insert_Webpage(request):
    tlo=Topic.objects.all()
    d={'topic':tlo}
    if request.method=='POST':
        tn=request.POST.get('tn')
        nam=request.POST['nm']
        emi=request.POST['em']
        Urs=request.POST['ur']
        to=Topic.objects.get_or_create(Topic_name=tn)[0]
        wlo=Webpage.objects.get_or_create(Topic_name=to,name=nam,email=emi,url=Urs)[0]
        wlo.save()
        return HttpResponse("Successfully data submitted!!!")

    return render(request,'Insert_Webpage.html',d)

def Insert_Access(request):
    wlo=Webpage.objects.all()
    d={'webs':wlo}
    if request.method=='POST':
        nm=request.POST.get('nm')
        Spou=request.POST['sp']
        dat=request.POST['dt']
        wo=Webpage.objects.get_or_create(name=nm)[0]
        alo=AccessRecord.objects.get_or_create(name=wo,Spouncer=Spou,Date=dat)[0]
        alo.save()
        return HttpResponse("Successfully data is submitted!!!")

    return render(request,'Insert_Access.html',d)

def Retrieve_Webpage(request):
    tlo=Topic.objects.all()
    d={'topics':tlo}
    if request.method=='POST':
        to=request.POST.getlist('tn')
        emptys=Webpage.objects.none()
        for a in to:
            emptys=emptys|Webpage.objects.filter(Topic_name=a)
        d1={'webs':emptys}
        return render(request,'Display_Webpage.html',d1)

    return render(request,'Retrieve_Webpage.html',d)

def Retrieve_Access(request):
    wlo=Webpage.objects.all()
    d={'webs':wlo}
    if request.method=='POST':
        wo=request.POST.getlist('nm')
        emptys=AccessRecord.objects.none()
        for a in wo:
            emptys=emptys|AccessRecord.objects.filter(name=a)
        d1={'Access':emptys}
        return render(request,'Display_Access.html',d1)

    return render(request,'Retrieve_Access.html',d)