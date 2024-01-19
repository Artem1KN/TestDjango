from django.shortcuts import render

from django.http import HttpResponse

import re
import requests

# Create your views here.

def index(request):
    return render(request, "index.html")

def home_page(request):
    return render(request, 'HomePage.html',
                  {'navigation': get_navigation_data(), 'context': get_main_page_data()})