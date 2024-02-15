import datetime
from django.core.management.base import BaseCommand
from store_app.models import Client


class Command(BaseCommand):
    help = 'Fill clients'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(count):
            client = Client(
                name=f'Client {i}',
                email=f'client{i}@example.com',
                phone_number=f'8-990-456-98-0{i}',
                address=f'Address {i}',
                registration_date=datetime.date(2022, 1, 5),
            )
            client.save()
        self.stdout.write(str(f'{count} created clients'))

