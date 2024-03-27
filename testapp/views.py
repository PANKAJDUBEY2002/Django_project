from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greeting(request):
    s="<h1>hello and welcome to first view of testapp</h1>"
    s+="This is landing page"
    return HttpResponse(s)
def showContact(request):
    s="<h1>Contact Page</h1>"
    s+="<p>website: pankaj.com</p>"
    s+="<p>mobile: 38377748</p>"
    s+="<p>Email: pankaj@gmail.com</p>"
    return HttpResponse(s)
def about(request):
    s="<h1>This is an about page</h1>"
    return HttpResponse(s)
