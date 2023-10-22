from django.urls import path
from . import views

urlpatterns = [
    path('game_list/', views.gameViews, name='gameList'),
    path('game_detail/<int:id>/', views.gameDetailInfo, name='detail'),
    path('game_detail/<int:id>/delete/', views.deleteGameView, name='delete'),
    path('game_detail/<int:id>/update/', views.updateGameView, name='update'),
    path('create_game/', views.gameCreateView, name='createGame'),
]