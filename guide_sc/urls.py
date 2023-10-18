from django.contrib import admin
from django.urls import path
from guide_sc import views

app_name = 'guide_sc'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.person, name='home'),
]