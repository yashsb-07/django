from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request, 'shop/index.html')

def about(request):
    return HttpResponse ('We are at about us page')

def contact(request):
    return HttpResponse ('We are at contact us page')
 
def tracker(request):
    return HttpResponse ('We are at tracker page')

def search(request):
    return HttpResponse ('We are at search page')
    
def productview(request):
    return HttpResponse ('We are at product view page')
    
def checkout(request):
    return HttpResponse ('We are at checkout page')

    