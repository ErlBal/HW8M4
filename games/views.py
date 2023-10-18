from django.shortcuts import render, get_object_or_404
from . import models

def gameViews(request):
    gameVal = models.Games.objects.all()
    html_name = 'games/games_list.html'
    context = {
        'game_key': gameVal,
    }
    return render(request, html_name, context)


def gameDetailInfo(request, id):
    game_id = get_object_or_404(models.Games, id=id)
    html_name = 'games/games_detail.html'
    context = {
        'game_id': game_id,
    }
    return render(request, html_name, context)