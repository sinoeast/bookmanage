import json
import time

from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse

#
def gengmulu(req):
    #namespace:name 通过别名反向解析路由
    rout = reverse('book:xx')
    print(rout)
    return HttpResponse('根目录')

def jiexiluyou(req,id,name):
    #namespace:name 通过别名反向解析路由
    rout = reverse('book:zz',kwargs={"id":id,"name":name})
    print(rout)
    return HttpResponse(f'解析路由是{id}/{name}' )

def get(reqest):
    # QueryDict的get方法只能获取 key 的最后一个值
    get = reqest.GET
    print(get)
    query_dict = get.get('name')
    query_dict1 = get.getlist('name')
    # dict = {
    #     'name':['1','2']
    # }
    # print(dict['name'])
    print(query_dict)
    print(query_dict1)
    return HttpResponse("请求的name值是{}".format(query_dict1))


def post(reqest):
    # form-data
    get = reqest.POST
    print(get)
    try:
        name = get['name']
    except :
        print("没有使用form-data name参数")


    #Json数据 （非表单类型 Non-Form Data 可以通过request.body属性获取最原始的请求体数据，自己按照请求体格式（JSON、XML等）进行解析。request.body返回bytes类型）
    bjson: bytes = reqest.body
    print(bjson)
    # str_json: str = bjson.decode() 3.6版本支持；loads直接用字节码了
    dict_json: dict = json.loads(bjson)



    # 其他常用HttpRequest对象属性
    # request.META属性获取请求头headers中的数据，request.META为字典类型。
    # method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'。
    # user：请求的用户对象。
    # path：一个字符串，表示请求的页面的完整路径，不包含域名和参数部分。
    # encoding：一个字符串，表示提交的数据的编码方式。
    #
    # 如果为None则表示使用浏览器的默认设置，一般为utf - 8。
    # 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值。
    # FILES：一个类似于字典的对象，包含所有的上传文件。


    #####################################################HttpResponse###################################################
    rout = reverse('book:xx')
    # return redirect(rout)#利用路由重定向
    # return JsonResponse(dict_json)#返回json数据
    return HttpResponse(f"{dict_json}")# 返回的字符串数据HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)


def set_cookie(req):
    req_body = req.body
    dict_req = json.loads(req_body)
    name = dict_req.get('name')
    response = HttpResponse('setcookie')
    response.set_cookie('name',name)

    return response