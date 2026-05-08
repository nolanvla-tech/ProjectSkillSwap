from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

ADMIN_USERNAME = 'nolan1'
ADMIN_PASSWORD = 'admin1234'


class Command(BaseCommand):
    help = 'Create the default admin user if they do not exist'

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(username=ADMIN_USERNAME)
        user.set_password(ADMIN_PASSWORD)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        if created:
            self.stdout.write(f'Superuser "{ADMIN_USERNAME}" created successfully.')
        else:
            self.stdout.write(f'Superuser "{ADMIN_USERNAME}" updated successfully.')
