from django.core.management.base import BaseCommand
from store_app.models import Products
import random


class Command(BaseCommand):
    help = 'Creates product'

    def handle(self, *args, **kwargs):
        for i in range(1, 9):
            product = Products(
                name=f'Product {i}',
                description=f'Description {i}',
                price=random.randint(1, 1000),
                quantity=random.randint(1, 10),
                date_added=f'2022-01-0{i}',
            )
            product.save()
        self.stdout.write(str(f'{i} created products'))