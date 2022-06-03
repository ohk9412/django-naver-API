from django.http.request import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
import json 
import pandas as pd
import os
import sys
import urllib.request
import matplotlib.pyplot as plt


client_id = "your key"
client_secret = "your key"


def shopping_cate(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    time = request.GET.get('term')
    if(request.GET.get('SUB')=='1'):
        Param = request.GET.get('SUB1')
    elif(request.GET.get('SUB')=='2'):
        Param = request.GET.get('SUB2')
    elif(request.GET.get('SUB')=='3'):
        Param = request.GET.get('SUB3')
    else:
        Param = request.GET.get('SUB4')

    url = "https://openapi.naver.com/v1/datalab/shopping/categories";
    body = "{\"startDate\":\"%s\",\"endDate\":\"%s\",\"timeUnit\":\"%s\",\"category\":[{\"name\":\"패션의류\",\"param\":[\"%s\"]}],\"device\":\"pc\",\"ages\":[\"20\",\"30\"],\"gender\":\"\"}"%(start, end, time, Param)

    requests = urllib.request.Request(url)
    requests.add_header("X-Naver-Client-Id",client_id)
    requests.add_header("X-Naver-Client-Secret",client_secret)
    requests.add_header("Content-Type","application/json")
    response = urllib.request.urlopen(requests, data=body.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        res = response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
    data = json.loads(res)
    datas = pd.DataFrame(data['results'][0]['data'])

    datas = datas.set_index("period")
    plt.figure( figsize=(6,3))
    plt.plot( datas.ratio )
    plt.savefig('C:\work\django1\mysite\static\shopping_cate.png')

    url = "https://openapi.naver.com/v1/datalab/shopping/category/device";
    body = body = "{\"startDate\":\"%s\",\"endDate\":\"%s\",\"timeUnit\":\"%s\",\"category\":\"%s\",\"ages\":[\"20\",\"30\"],\"gender\":\"\"}"%(start, end, time, Param)

    requests = urllib.request.Request(url)
    requests.add_header("X-Naver-Client-Id",client_id)
    requests.add_header("X-Naver-Client-Secret",client_secret)
    requests.add_header("Content-Type","application/json")
    response = urllib.request.urlopen(requests, data=body.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        res = (response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
    data = json.loads(res)
    datas = pd.DataFrame(data['results'][0]['data'])

    # datas = datas.set_index("period")
    datas = pd.pivot_table(datas,
               index = 'group',
               #피벗 테이블은 기본적으로 수치만 포함
               #기본 연산은 평균을 사용한다.
               # 만약 바꾸려면 
               aggfunc='sum'
               #aggfunc=['sum','mean']
               )[['ratio']]
    plt.figure( figsize=(6,3))
    plt.pie( datas.ratio, labels=datas.index ,autopct='%.1f%%',textprops={'fontsize': 30} )
    plt.savefig('C:\work\django1\mysite\static\shopping_device.png')


    url = "https://openapi.naver.com/v1/datalab/shopping/category/gender";
    body = "{\"startDate\":\"%s\",\"endDate\":\"%s\",\"timeUnit\":\"%s\",\"category\":\"%s\",\"ages\":[\"20\",\"30\"],\"device\":\"\" }"%(start, end, time, Param)

    requests = urllib.request.Request(url)
    requests.add_header("X-Naver-Client-Id",client_id)
    requests.add_header("X-Naver-Client-Secret",client_secret)
    requests.add_header("Content-Type","application/json")
    response = urllib.request.urlopen(requests, data=body.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        res = (response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
    data = json.loads(res)
    datas = pd.DataFrame(data['results'][0]['data'])

    # datas = datas.set_index("period")
    datas = pd.pivot_table(datas,
               index = 'group',
               #피벗 테이블은 기본적으로 수치만 포함
               #기본 연산은 평균을 사용한다.
               # 만약 바꾸려면 
               aggfunc='sum'
               #aggfunc=['sum','mean']
               )[['ratio']]
    plt.figure( figsize=(6,3))
    plt.pie( datas.ratio, labels=datas.index ,autopct='%.1f%%',textprops={'fontsize': 30} )
    plt.savefig('C:\work\django1\mysite\static\shopping_gender.png')

    return render(request, 'shopping/main.html')

# data = shopping_cate()

# data = data.set_index("period")

# plt.figure( figsize=(12,6))

# plt.plot( data.ratio )

# plt.show()

