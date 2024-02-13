from django.core.management.base import BaseCommand
from store_app.models import Client


class Command(BaseCommand):
    help = 'Creates client'

    def handle(self, *args, **kwargs):
        for i in range(1, 9):
            client = Client(
                name=f'Client {i}',
                email=f'client{i}@example.com',
                phone_number=f'8-990-456-98-0{i}',
                address=f'Address {i}',
                registration_date=f'2022-01-0{i}',
            )
            client.save()

        self.stdout.write(str(f'{i} created clients'))