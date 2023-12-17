from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from habits.models import Habits
from habits.pagination import HabitPaginator
from habits.permissions import IsPublic, IsOwner
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания привычки"""

    serializer_class = HabitSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # сохранение пользователя в привычку
        serializer.save(user=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    """Контроллер для списка привычек"""

    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated & IsOwner, IsAdminUser]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра привычки"""

    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsPublic]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для обновления привычки"""

    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsOwner, IsAdminUser]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления привычки"""

    queryset = Habits.objects.all()
    permission_classes = [IsOwner, IsAdminUser]