from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import pymongo
# Create your views here.

def mainpage(request):
    return render(request, "mainpage.html")

def add_visitor():
    ...