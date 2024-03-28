from django.urls import path
from testapp import views

urlpatterns=[
     path('about',views.about),
     path('contact',views.showContact),
     path('',views.greeting),
]
