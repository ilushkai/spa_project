from django.test import TestCase
from django.utils import timezone
from .validators import *
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Habits

class HabitsValidatorsTestCase(TestCase):
    def test_related_habit_and_reward_validator(self):
        habit = Habits(related_habit=Habits(), reward="Награда")
        with self.assertRaises(ValidationError) as context:
            validate_related_habit_and_reward(habit)
        self.assertEqual(context.exception.message, "Нельзя одновременно выбирать связанную привычку и награду.")

    def test_execution_time_validator(self):
        habit = Habits(execution_time=timezone.timedelta(minutes=3))
        with self.assertRaises(ValidationError) as context:
            validate_execution_time(habit)
        self.assertEqual(context.exception.message, "Время выполнения не должно превышать 2 минут.")

    def test_related_habit_for_pleasurable_habit_validator(self):
        habit = Habits(good_habit_sign=True, related_habit=Habits(good_habit_sign=False))
        with self.assertRaises(ValidationError) as context:
            validate_related_habit_for_pleasurable_habit(habit)
        self.assertEqual(context.exception.message, "Связанная привычка должна быть приятной для данной привычки.")

    def test_pleasurable_habit_constraints_validator(self):
        habit = Habits(good_habit_sign=True, reward="Награда")
        with self.assertRaises(ValidationError) as context:
            validate_pleasurable_habit_constraints(habit)
        self.assertEqual(context.exception.message, "Приятные привычки не могут иметь награды или связанных привычек.")

    def test_habit_frequency_validator(self):
        habit = Habits(periodicity=5)
        with self.assertRaises(ValidationError) as context:
            validate_habit_frequency(habit)
        self.assertEqual(context.exception.message, "Привычка должна выполняться хотя бы раз в 7 дней.")



class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="4@admin.ru", password="spartak67", is_active=True, is_superuser=True
        )
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.habit = Habits.objects.create(
            id=1,
            place="Работа",
            time="00:00",
            activity="Попить воды",
            good_habit_sign=False,
            periodicity=2,
            reward="",
            execution_time="00:01:00",
            of_publicity=False,
            user=self.user,
            relted_habbit=None,
        )
        self.habit.save()

    def test_create_habit(self):
        data = {
            'place': 'Дом',
            'activity': 'Физическая активность',
            'reward': 'Здоровый образ жизни',
            'publicity': True,
            'time': '14:00:00',
            'good_habit_sign': True,
            'periodicity': 3,
            'execution_time': '00:10:00',
        }
        response = self.client.post('/habits/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habits.objects.count(), 1)
        self.assertEqual(Habits.objects.get().user, self.user)

    def test_list_habits(self):
        habit = Habits.objects.create(place='Тренажерный зал', activity='Бег', user=self.user)
        response = self.client.get('/habits/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_habit(self):
        habit = Habits.objects.create(place='Тренажерный зал', activity='Бег', user=self.user)
        response = self.client.get(f'/habits/{habit.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['activity'], 'Бег')

    def test_update_habit(self):
        habit = Habits.objects.create(place='Тренажерный зал', activity='Бег', user=self.user)
        data = {'activity': 'Пробежка'}
        response = self.client.put(f'/habits/{habit.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habits.objects.get().activity, 'Пробежка')

    def test_delete_habit(self):
        habit = Habits.objects.create(place='Тренажерный зал', activity='Бег', user=self.user)
        response = self.client.delete(f'/habits/{habit.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habits.objects.count(), 0)

