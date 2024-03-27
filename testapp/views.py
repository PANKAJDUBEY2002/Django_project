from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greeting(request):
    s="<h1>hello and welcome to first view of testapp</h1>"
    return HttpResponse(s)
