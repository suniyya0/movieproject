# movie_recommendation/urls.py
from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from movies.views import home
from django.contrib.auth import views as auth_views
from users.views import edit_profile, profile

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URLs
    path('users/', include('users.urls')),  # Include users app URLs under '/users/'
    path('movies/', include('movies.urls')),  # Include movies app URLs under '/movies/'
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('profile/', profile, name='profile'),  # Define profile URL
    path('', include('movies.urls')),
    path('', home, name='home'),
    path('profile/edit/', edit_profile, name='edit_profile'),
        # Default ded
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
