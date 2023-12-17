# Generated by Django 5.0 on 2023-12-13 12:52

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=200, null=True, verbose_name='место')),
                ('activity', models.CharField(blank=True, max_length=300, null=True, verbose_name='действие')),
                ('reward', models.CharField(blank=True, max_length=200, null=True, verbose_name='награда')),
                ('publicity', models.BooleanField(default=False, verbose_name='публичность')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='Время выполнения привычки')),
                ('good_habit_sign', models.BooleanField(default=False, verbose_name='признак приятной привычки')),
                ('periodicity', models.IntegerField(default=1, verbose_name='периодичность')),
                ('execution_time', models.TimeField(default='01:00', verbose_name='время на выполнение')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habits', verbose_name='Связанная привычка')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
                'ordering': ['time'],
            },
        ),
    ]
