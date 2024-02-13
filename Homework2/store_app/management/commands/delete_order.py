from django.core.management.base import BaseCommand
from store_app.models import Order


class Command(BaseCommand):
    help = 'Deletes order by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        self.stdout.write(f'{order} deleted')
        order.delete()