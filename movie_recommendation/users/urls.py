from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Example: /users/register/
    path('register/', views.register, name='register'),
    path('login/', views.login_View, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/', views.view_profile, name='view_profile'),
    # Add more URL patterns as needed
]
