from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Отдельная страница с информацией о постах
    path('group/<slug:pk>/', views.group_posts),
] 
