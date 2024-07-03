
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # Customize how User model is displayed in the admin panel
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(User, CustomUserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    pass

# Register your models here.
