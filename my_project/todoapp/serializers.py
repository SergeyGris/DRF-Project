from rest_framework.serializers import ModelSerializer

from .models import Project, ToDo
from usersapp.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)
    users = UserModelSerializer(source='project', many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    project = ProjectModelSerializer()
    creator = UserModelSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'
