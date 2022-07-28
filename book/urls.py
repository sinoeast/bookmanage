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
    path('<int:i>', views.xx)
]