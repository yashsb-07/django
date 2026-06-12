from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello Yash. You are learning Django")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello Yash. You are on about page")

def contact(request):
    return HttpResponse("Hello Yash. You are on contact page")