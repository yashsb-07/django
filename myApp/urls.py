from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_games, name='all_games'),
    path('<int:game_id>/', views.game_details, name='game_details'),
]