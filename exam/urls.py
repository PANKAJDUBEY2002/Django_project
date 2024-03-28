from django.urls import path
from exam import views

urlpatterns=[
     path('test',views.showTest),
     path('result',views.showResult),
]
