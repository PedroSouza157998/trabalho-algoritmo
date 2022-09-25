from django.shortcuts import render
from django.http import HttpResponse
import os


# Create your views here.

def index(request):
    print(os.system("ls"))
    return HttpResponse(open('home/view/interface.html', 'r').read())