from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        PROVIDER = "PROVIDER", "Provider"

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER,
    )

    def __str__(self):
        return self.username
