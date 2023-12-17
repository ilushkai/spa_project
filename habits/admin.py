from django.contrib import admin

from habits.models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "activity",
        "reward",
        "of_publicity",
        "time",
        "good_habit_sign",
        "periodicity",
        "execution_time",
    )  # отображение
    list_filter = ("place", "user", "activity", "reward")  # фильтр
    search_fields = ("place", "user", "activity", "reward")  # поля поиска