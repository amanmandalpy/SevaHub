from rest_framework import serializers

from .models import ServiceCategory, Service


class ServiceCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceCategory
        fields = [
            "id",
            "name",
            "description",
            "is_active",
        ]


class ServiceSerializer(serializers.ModelSerializer):

    provider_name = serializers.CharField(
        source="provider.username",
        read_only=True,
    )

    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
    )

    class Meta:
        model = Service
        fields = [
            "id",
            "provider",
            "provider_name",
            "category",
            "category_name",
            "name",
            "description",
            "price",
            "duration_minutes",
            "is_active",
        ]

        read_only_fields = [
            "provider",
        ]
