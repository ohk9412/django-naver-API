from typing import get_type_hints
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
import json 
import pandas as pd
import os
import sys
import urllib.request
import matplotlib.pyplot as plt


def index(request):
    return render(request, 'searchkeyword/style.html')




    
    

