from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCustomViewSet

users_router = DefaultRouter()
users_router.register('users', UserCustomViewSet)
