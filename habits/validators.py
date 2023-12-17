from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import timedelta

def validate_related_habit_and_reward(habit):
    """
    Валидатор, проверяющий, что не выбраны одновременно связанная привычка и вознаграждение.
    """
    if habit.related_habit and habit.reward:
        raise ValidationError(_("Нельзя одновременно выбирать связанную привычку и награду."))

def validate_execution_time(habit):
    """
    Валидатор, проверяющий, что время выполнения не превышает 2 минут.
    """
    if habit.execution_time > timedelta(minutes=2):
        raise ValidationError(_("Время выполнения не должно превышать 2 минут."))

def validate_related_habit_for_pleasurable_habit(habit):
    """
    Валидатор, проверяющий, что связанная привычка может быть выбрана только для приятных привычек.
    """
    if habit.related_habit and not habit.related_habit.good_habit_sign:
        raise ValidationError(_("Связанная привычка должна быть приятной для данной привычки."))

def validate_pleasurable_habit_constraints(habit):
    """
    Валидатор, проверяющий ограничения для приятных привычек.
    """
    if habit.good_habit_sign and (habit.reward or habit.related_habit):
        raise ValidationError(_("Приятные привычки не могут иметь награды или связанных привычек."))

def validate_habit_frequency(habit):
    """
    Валидатор, проверяющий, что привычка не может выполняться реже, чем 1 раз в 7 дней.
    """
    if habit.periodicity < 7:
        raise ValidationError(_("Привычка должна выполняться хотя бы раз в 7 дней."))
