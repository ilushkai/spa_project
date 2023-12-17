from django.db import models
from users.models import NULLABLE, User
from django.utils import timezone
from habits.validators import *


class Habits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user",
                             **NULLABLE, verbose_name="пользователь", )
    place = models.CharField(max_length=200, **NULLABLE, verbose_name="место")
    activity = models.CharField(max_length=300, **NULLABLE, verbose_name="действие")
    reward = models.CharField(max_length=200, **NULLABLE, verbose_name="награда")
    publicity = models.BooleanField(default=False, verbose_name="публичность")
    time = models.TimeField(
        default=timezone.now, verbose_name="Время выполнения привычки"
    )
    good_habit_sign = models.BooleanField(
        default=False, verbose_name="признак приятной привычки"
    )
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, verbose_name="Связанная привычка", **NULLABLE
    )
    periodicity = models.IntegerField(default=1, verbose_name="периодичность")
    execution_time = models.TimeField(
        default="01:00", verbose_name="время на выполнение"
    )

    def __str__(self):
        return f"{self.user}, {self.place}, {self.time}"

    def clean(self):
        """
        Метод для валидации полей модели перед сохранением в базу данных.
        """
        validate_related_habit_and_reward(self)
        validate_execution_time(self)
        validate_related_habit_for_pleasurable_habit(self)
        validate_pleasurable_habit_constraints(self)
        validate_habit_frequency(self)

    def save(self, *args, **kwargs):
        """
        Метод для сохранения объекта модели с предварительной валидацией.
        """
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
        ordering = ["time"]
