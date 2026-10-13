from django.urls import path

from .views import (
    ServiceCategoryListCreateView,
    ServiceListCreateView,
    ServiceDetailView,
)

urlpatterns = [
    path(
        "categories/",
        ServiceCategoryListCreateView.as_view(),
        name="category-list-create",
    ),
    path(
        "",
        ServiceListCreateView.as_view(),
        name="service-list-create",
    ),
    path(
        "<int:pk>/",
        ServiceDetailView.as_view(),
        name="service-detail",
    ),
]
