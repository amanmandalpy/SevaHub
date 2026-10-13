from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import ServiceCategory, Service
# Register your models here.

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_active',
        'created_at'
    )

    list_filter = ('is_active',)

    search_fields = ('name',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "provider",
        "category",
        "price",
        "duration_minutes",
        "is_active",
        "created_at",

    )
    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "name",
        "description",
        "provider_username",
    )
>>>>>>> a1c08e27222c45bde2fdeb163e681f07e78afec9
