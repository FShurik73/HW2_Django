from django.core.management.base import BaseCommand
from store_app.models import Products


class Command(BaseCommand):
    help = 'Deletes product by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Products.objects.filter(pk=pk).first()
        self.stdout.write(f'{product} deleted')
        product.delete()