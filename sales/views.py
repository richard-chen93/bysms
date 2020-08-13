from django.shortcuts import render
from django.http import HttpResponse
from common.models import Customer

# Create your views here.

def listoders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")

def index(request):
    return HttpResponse("this is default index page.")


def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Customer.objects.values()

    #检查url get请求中是否有参数phone number
    pn = request.GET.get('phonenumber',None)

    #如果有，添加过滤条件
    if pn:
        qs = qs.filter(phonenumber=pn)  

    # 定义返回字符串
    retStr = ''
    for customer in  qs:
        for name,value in customer.items():
            retStr += f'{name} : {value} | '
        # <br> 表示换行
        retStr += '<br>'


    return HttpResponse(retStr)