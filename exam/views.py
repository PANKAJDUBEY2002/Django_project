from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def showTest(request):
    res=render(request,'exam/test.html')
    return res
def showResult(request):
    s="<h1>This is show result page</h1>"
    return HttpResponse(s)
