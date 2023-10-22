from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms

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

def gameCreateView(request):
    method = request.method
    if method == "POST":
        form = forms.GamesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Игра успешно добавлена')

    else:
        form = forms.GamesForm()

    return render(request, 'games/create_game.html', {'form': form})

def deleteGameView(request, id):
    game_id = get_object_or_404(models.Games, id=id)
    game_id.delete()
    return HttpResponse('Игра успешно удалена')

def updateGameView(request, id=id):
    game_id = get_object_or_404(models.Games, id=id)
    if request.method == 'POST':
        form = forms.GamesForm(instance=game_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Игра изменена')

    else:
        form = forms.GamesForm(instance=game_id)
    return render(request, 'games/update_game.html',
                         {
                      'form': form,
                      'game_id': game_id
                         }
                 )
