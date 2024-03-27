from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def showTest(request):
    s="<h1>This is show test case page</h1>"
    return HttpResponse(s)
def showResult(request):
    s="<h1>This is show result page</h1>"
    return HttpResponse(s)
