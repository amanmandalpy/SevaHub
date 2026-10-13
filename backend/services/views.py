<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Service, ServiceCategory
from .serializers import (
    ServiceCategorySerializer,
    ServiceSerializer,
)


class ServiceCategoryListCreateView(generics.ListCreateAPIView):
    queryset = ServiceCategory.objects.filter(is_active=True)
    serializer_class = ServiceCategorySerializer
    permission_classes = [IsAuthenticated]


class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = Service.objects.select_related(
        "provider",
        "category",
    )
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(provider=self.request.user)


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.select_related(
        "provider",
        "category",
    )
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Service.objects.select_related(
            "provider",
            "category",
        ).filter(provider=self.request.user)
>>>>>>> a1c08e27222c45bde2fdeb163e681f07e78afec9
