from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def listoders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")

def index(request):
    return HttpResponse("this is default index page.")
