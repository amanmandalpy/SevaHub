<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from rest_framework import generics

from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer



class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
>>>>>>> a1c08e27222c45bde2fdeb163e681f07e78afec9
