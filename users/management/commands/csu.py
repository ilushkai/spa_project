from django.core.management import BaseCommand

from users.models import User


# создание админа
class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@adm.ru",
            first_name="Admin",
            last_name="Admin",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        user.set_password("1q2w!Q@W")  # установка пароля
        user.save()  # сохраниние в БД