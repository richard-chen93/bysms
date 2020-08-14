from django.http import JsonResponse
from common.models import Customer
import json

def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST','PUT','DELETE']:
        request.params = json.loads(request.body)

    action = request.params['action']
    if action == 'list_customer':
        return listcustomer(request)
    elif action =='add_customer':
        return addcustomer(request)
    elif action == 'modify_customer':
        return modifycustomer(request)
    elif action == 'del_customer':
        return deletecustomer(request)

    else:
        return JsonResponse({'ret':1,'msg':'不支持该类型http请求'})

def listcustomer(request):
    # 返回一个QuerySet对象，包含所有的表记录
    qs = Customer.objects.values()

    #将Queryset对象转化为list类型，否则不能被转化为Json字符串
    retlist = list(qs)

    return JsonResponse({'ret':0,'retlist':retlist})
def addcustomer(request):
    info = request.params['data']
    #从请求消息中，获取要添加客户的信息，并插入到数据库中
    record = Customer.objects.create(name=info['name'],
                            phonenumber=info['phonenumber'],
                            address=info[address])
    return JsonResponse({'ret':0},{'id':record.id})