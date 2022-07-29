#!/usr/bin/python3
# -*- coding:utf-8 -*-
""""
  @Author: 蓝天
  @Email: lantian27294@hundsun.com
  @Time: 2022/7/28 10:01
  @File: urls.py
"""
from django.urls import path

from book import views

urlpatterns = [
    # name 用于反向解析路由
    path('', views.gengmulu, name='xx'),
    path('<int:id>/<str:name>/', views.jiexiluyou, name='zz'),
    path('get/', views.get, name='get'),
    path('post/', views.post, name='post'),
    path('set_cookie', views.set_cookie, name='set_cookie'),
]
