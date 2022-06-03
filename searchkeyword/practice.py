from django.http.request import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
import json 
import numpy as np
import pandas as pd
import os
import sys
import urllib.request
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib




client_id = "your key"
client_secret = "your key"


def complete(request):
    item_keyword1 = request.GET.get('item_keyword1')
    item_sub_keyword1_1 = request.GET.get('item_sub_keyword1_1')
    startYearInput = request.GET.get('startYearInput')
    startMonthInput = request.GET.get('startMonthInput')
    startDayInput = request.GET.get('startDayInput')
    endYearInput = request.GET.get('endYearInput')
    endMonthInput = request.GET.get('endMonthInput')
    endDayInput = request.GET.get('endDayInput')

    url = "https://openapi.naver.com/v1/datalab/search";
    body = "{\"startDate\":\"%s-%s-%s\",\"endDate\":\"%s-%s-%s\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"%s\",\"keywords\":[\"%s\"]}]}"%(startYearInput,startMonthInput,startDayInput,endYearInput,endMonthInput,endDayInput,item_keyword1,item_sub_keyword1_1)

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

    datas = datas.set_index("period")
    plt.figure( figsize=(6,3))
    plt.yticks([25,50,75,100])
    plt.plot(datas.ratio)
    plt.savefig('C:\work\django1\mysite\static\search.png')



    pageNum = 1
    query= urllib.parse.quote(item_keyword1)
    q = []
    

    for i in range(4):
        target_site = f'https://search.shopping.naver.com/search/all?query={query}&pagingIndex={pageNum}&pagingSize=40&productSet=total'
        pageNum +=1
        url = target_site
        res = urlopen(url)
        soup = BeautifulSoup(res, 'html5lib')
            
        for td in soup.select('.basicList_title__3P9Q7'):   
            q.append(td.a.string.strip())

        
    



    return render(request, 'searchkeyword/style.html', {'q':q})
    # HttpResponse(q)
    














