import os
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a superuser from environment variables if one does not exist'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not username or not password:
            self.stdout.write('Skipping: DJANGO_SUPERUSER_USERNAME or DJANGO_SUPERUSER_PASSWORD not set.')
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(f'Superuser "{username}" already exists, skipping.')
            return

        User.objects.create_superuser(username=username, email='', password=password)
        self.stdout.write(f'Superuser "{username}" created successfully.')
