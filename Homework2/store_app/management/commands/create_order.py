from django.core.management.base import BaseCommand
from store_app.models import Products, Order, Client
import random

from random import choice


class Command(BaseCommand):
    help = 'Creates order'

    def handle(self, *args, **kwargs):

        client_id = random.randint(1, 9)
        product_id_list = [1, 2, 3, 4, 5, 6, 7, 8]
        print(product_id_list)
        total_sum = 0
        products = []
        for product_id in product_id_list:
            product = Products.objects.filter(pk=product_id).first()
            products.append(product)
            total_sum += product.price
        client = Client.objects.filter(pk=client_id).first()
        order = Order(
            client=client,
            total_sum=total_sum,
        )
        order.save()
        for product in products:
            order.product.add(product)

        self.stdout.write(f'{order}')





