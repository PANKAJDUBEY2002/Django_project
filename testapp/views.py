from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
# Create your views here.
def employee_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    res=render(request,'testapp/employees.html',data)
    return res
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
    msg="This is an about page"
    return render(request,'testapp/about.html',{'msg':msg})
