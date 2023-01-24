from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectModelViewSet, ToDoModelViewSet

projects_router = DefaultRouter()
projects_router.register('', ProjectModelViewSet)

todo_router = DefaultRouter()
todo_router.register('', ToDoModelViewSet)
