from django.core.management.base import BaseCommand
from store_app.models import Client


class Command(BaseCommand):
    help = 'Update client'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client id')
        parser.add_argument('name', type=str, help='Client name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        client = Client.objects.filter(pk=pk).first()
        client.name = name
        client.save()
        self.stdout.write(str(f'{client} updated'))