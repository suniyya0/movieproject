from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('add/', views.add_movie, name='add_movie'),
    path('<int:pk>/', views.movie_detail, name='movie_detail'),
    path('<int:pk>/edit/', views.edit_movie, name='edit_movie'),
    path('<int:pk>/delete/', views.delete_movie, name='delete_movie'),
    path('movie/<int:movie_id>/profile/', views.movie_profile, name='movie_profile'),
    path('home/', views.home, name='home'),
    path('', home, name='home'),
    path('', views.movie_list, name='movie-list'),
    path('', views.movie_list, name='movie-list'),
]
