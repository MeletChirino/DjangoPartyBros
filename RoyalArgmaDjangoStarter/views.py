"""Views file for Django"""
#Django modules
from django.template import Template, Context, loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from apps.RoyalArgmaPartyBros.common import BOARDS

def home(request):
    """landing page para iniciar el juego"""
    return render(
        request,
        'home.html',
        context={"boards": BOARDS},
        )

def save_game(request):
    if request.METHOD == "POST":
        # Here you must save the game with an ID, and how many player are going to play
        pass
    else:
        # Redirect home
        pass

def single_player_sign_up(request, game_id):
    # Here you get the player the game ID and you save the player to that game
    pass
