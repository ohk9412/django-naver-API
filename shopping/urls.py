from django.urls import path
from . import views, main

app_name = 'shopping'

urlpatterns = [
    path('', views.main , name='main'),
    path('main/', main.shopping_cate , name='main_cete'),
]