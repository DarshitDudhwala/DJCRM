from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('<h1>This is home page</h1>')
