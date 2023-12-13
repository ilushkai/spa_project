from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone",
        "first_name",
    )  # отображение на дисплее
    list_filter = ("email", "phone", "first_name")  # фильтр
    search_fields = ("email", "phone", "first_name")  # поля поиска