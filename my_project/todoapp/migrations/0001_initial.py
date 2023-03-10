# Generated by Django 4.1.5 on 2023-01-23 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usersapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=64)),
                ('project_repo', models.URLField(blank=True)),
                ('user_list', models.ManyToManyField(related_name='projects', to='usersapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='usersapp.user')),
            ],
        ),
    ]
