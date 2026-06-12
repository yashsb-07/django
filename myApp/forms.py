from django import forms
from .models import GameVarity

class GameVarietyForm(forms.Form):
    game_variety = forms.ModelChoiceField(queryset=GameVarity.objects.all(), label="Select Game Variety")