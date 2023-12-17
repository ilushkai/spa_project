from django.urls import path

from habits.apps import HabitsConfig
from habits.views import *

app_name = HabitsConfig.name

urlpatterns = [
    path("/", HabitListAPIView.as_view(), name="habit-list"),
    path("create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("detail/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit-detail"),
    path("delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit-delete"),
    path("update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit-update"),
]
