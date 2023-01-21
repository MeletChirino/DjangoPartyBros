"""Views file for Django"""
#Django modules
from django.template import Template, Context, loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Royal Argma modules
from apps.RoyalArgmaPartyBros.game_elements.meryl import Meryl

from apps.RoyalArgmaPartyBros.common import BOARDS, AVATARS

def home(request):
    """landing page para iniciar el juego"""
    if request.method == "POST":
        # Here you must save the game with an ID, and how many player are going to play
        board_name = request.POST['board']
        client = Meryl(Meryl.CLIENT)
        action = {
            'action': 0,
            'board': board_name,
        }
        client.send(action)
        return redirect('inscription')
    else:
        return render(
            request,
            'home.html',
            context={"boards": BOARDS},
            )


def single_player_sign_up(request):
    """Pagina para registrar jugadores en una partida"""
    if request.method == "POST":
        # Here you must save the game with an ID, and how many player are going to play
        player_name = request.POST['name']
        av_name = request.POST['av_name']
        client = Meryl(Meryl.CLIENT)
        action = {
            'action': 1,
            'name': player_name,
            'avatar': av_name,
        }
        client.send(action)
        return redirect('inscription')
    elif request.method == "GET":
        av_list = []
        for avatar in AVATARS:
            av_list.append([avatar, AVATARS[avatar]])
        return render(
            request,
            'player_signin.html',
            context={"av_list": av_list},
            )
