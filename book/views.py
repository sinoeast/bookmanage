import time

from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
# Create your views here.
from django.urls import reverse


def putong(req):
    #namespace:name 通过别名反向解析路由
    rout = reverse('book:xx')
    print(rout)
    return HttpResponse('iiiii')

def lujing(req,id,name):
    #namespace:name 通过别名反向解析路由
    rout = reverse('book:zz',kwargs={"id":id,"name":name})
    print(rout)
    return HttpResponse(id,name)

def get(reqest):
    # QueryDict的get方法只能获取 key 的最后一个值
    query_dict = reqest.GET.get('name')
    query_dict1 = reqest.GET.getlist('name')
    dict = {
        'name':['1','2']
    }
    print(dict['name'])
    print(query_dict)
    print(query_dict1)
    return HttpResponse("123")
