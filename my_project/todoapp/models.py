from django.db import models
from usersapp.models import User

DISABLED = 0
ENABLED = 1
STATUS_CHOICES = (
    (DISABLED, 'Disabled'),
    (ENABLED, 'Enabled'),
)


class Project(models.Model):
    project_name = models.CharField(max_length=64)
    project_repo = models.URLField(max_length=200, blank=True)
    user_list = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    status = models.BooleanField(choices=STATUS_CHOICES, default=ENABLED)

    def __str__(self):
        return self.text
