from django.shortcuts import render

# Create your views here.
def all_games(request):
    return render(request, 'myApp/all_games.html')