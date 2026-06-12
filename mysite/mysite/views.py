from django.http import HttpResponse

def index(request):
    return HttpResponse()

def about(request):
    return HttpResponse("About Page")