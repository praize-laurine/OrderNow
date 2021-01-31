from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'customer/index.html')

def about(request):
    return render(request, 'customer/about.html')    

