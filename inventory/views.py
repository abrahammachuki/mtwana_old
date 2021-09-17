from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from .models import device, allocation
import django_tables2 as tables


def homepage(request):
    return render(request, 'homepage.html')


#class deviceListView(ListView):
    #model = device
    #template_name = 'devices.html'


#class allocationListView(ListView):
    #model = allocation
    #template_name = 'allocations.html'


def deviceListManual(request):
    alldevices = device.objects.all()
    context = {'alldevices':alldevices}
    return render(request, 'devicelist.html', context)


def allocationListManual(request):
    allallocations = allocation.objects.all()
    context = {'allallocations':allallocations}
    return render(request, 'allocationlist.html', context)




