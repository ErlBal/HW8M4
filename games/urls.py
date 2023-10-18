from django.urls import path
from . import views

urlpatterns = [
    path('game_list/', views.gameViews, name='GameList'),
    path('game_detail/<int:id>', views.gameViews, name='detail'),
]