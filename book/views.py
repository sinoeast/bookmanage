from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def xx(req,i):
    return HttpResponse(i)