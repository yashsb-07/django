from django.shortcuts import render
from .models import GameVarity, Store
from django.shortcuts import get_object_or_404
from .forms import GameVarietyForm

# Create your views here.
def all_games(request):
    games = GameVarity.objects.all()
    return render(request, 'myApp/all_games.html', {'games': games})

def game_details(request, game_id):
    game = get_object_or_404(GameVarity, pk=game_id)
    return render(request, 'myApp/game_detail.html', {'game': game})

def game_store_view(request):
    stores = None
    if request.method == 'POST':
        form = GameVarietyForm(request.POST)
        if form.is_valid():
            game_variety = form.cleaned_data['game_variety']
            Store.objects.filter(game_varieties=game_variety)
    else:
        form = GameVarietyForm()
    return render(request, 'myApp/game_store.html', {'stores': stores, 'form': form})