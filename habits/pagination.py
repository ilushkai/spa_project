from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """Пагинации курсов"""

    page_size = 20  # количество элементов на странице