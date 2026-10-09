from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, ProviderProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "role",
        "phone",
        "is_active",
    )

    list_filter = (
        "role",
        "is_active",
    )

    search_fields = (
        "username",
        "email",
        "phone",
    )

@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = (
        "business_name",
        "user",
        "city",
        "experience_years",
        "is_verified",

    )

    list_filter = (
        "city",
        "is_verified",
    )

    search_fields = (
        "business_name",
        "user_username",
        "city",
    )

