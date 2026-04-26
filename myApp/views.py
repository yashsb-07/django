from django.shortcuts import render
from .models import GameVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_games(request):
    games = GameVarity.objects.all()
    return render(request, 'myApp/all_games.html', {'games': games})

def game_details(request, game_id):
    game = get_object_or_404(GameVarity, pk=game_id)
    return render(request, 'myApp/game_detail.html', {'game': game})