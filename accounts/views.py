from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    model = User
    permission_classes = [IsAdminUser,]


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    model = User


class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User
    permission_classes = [IsAuthenticated,]






