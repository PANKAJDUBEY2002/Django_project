from django.urls import path
from testapp import views

urlpatterns=[
     path('about',views.about),
     path('employee',views.employee_info_view),
     path('contact',views.showContact),
     path('',views.greeting),
]
