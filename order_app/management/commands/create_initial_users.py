from django.core.management.base import BaseCommand
from order_app.models import Employee


class Command(BaseCommand):
    help = "Create initial users if they do not exist"

    def handle(self, *args, **options):
        if not Employee.objects.filter(username="user1").exists():
            Employee.objects.create_user(
                username="user1", password="Password1", position="Senior Developer"
            )
            self.stdout.write(self.style.SUCCESS("User1 created successfully"))

        if not Employee.objects.filter(username="user2").exists():
            Employee.objects.create_user(
                username="user2", password="Password2", position="Middle Developer"
            )
            self.stdout.write(self.style.SUCCESS("User2 created successfully"))

        if not Employee.objects.filter(username="user3").exists():
            Employee.objects.create_user(
                username="user3",
                password="Password3",
                probation=True,
                position="Junior Developer",
            )
            self.stdout.write(self.style.SUCCESS("User3 created successfully"))
