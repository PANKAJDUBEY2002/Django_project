from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def showTest(request):
    que="Who developed C language?"
    a="ken thompson"
    b="Danis ritchie"
    c="Bjarne stroustrup"
    d="James gosling"
    data={'que':que,'a':a,'b':b,'c':c,'d':d}
    res=render(request,'exam/test.html',context=data)
    return res
def showResult(request):
    s="<h1>This is show result page</h1>"
    return HttpResponse(s)
