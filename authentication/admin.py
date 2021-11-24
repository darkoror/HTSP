from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentication.models import User


@admin.register(User)
class AdminUser(UserAdmin):
    list_display = (
        'username', 'email', 'is_active', 'is_staff', 'is_superuser',
    )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'is_superuser', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    list_filter = ('username', 'email', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email',)
    ordering = ('email',)
