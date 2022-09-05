from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):

   return render(request,'index.html')


def sentmessage(request):
    return render(request,'sentmessage.html')

def decipher(request):
    return render(request,'decipher.html')    