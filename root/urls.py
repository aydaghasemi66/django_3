from django.urls import path
from .views import *

app_name = 'root'

urlpatterns = [
    path("",home,name="home"),
    path('appointment/', appointment, name='appointment'),

]