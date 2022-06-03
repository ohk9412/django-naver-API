
from django.urls import path
from . import views, practice


app_name = 'searchkeyword'

urlpatterns = [
    path('', views.index, name='style'),
    path('searchkeyword/result/', practice.complete, name='complete'),


    

]