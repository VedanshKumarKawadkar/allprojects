from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mainpage(request):
    return render(request, "mainpage.html")