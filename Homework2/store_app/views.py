from datetime import datetime, timedelta
from .forms import ProductsForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Order, Products
import logging

logger = logging.getLogger(__name__)


def index(request, product_id: int):
    product = get_object_or_404(Products, pk=product_id)
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.quantity = form.cleaned_data['quantity']
            product.save()
            logger.info(f' {product.name=}, {product.description=}, {product.price=}, {product.quantity=}.')
            message = 'Товар успешно изменен'
            return render(request, "store_app/index.html", {'form': form, 'message': message})

    else:
        form = ProductsForm()
        message = 'Заполните форму'
        return render(request, "store_app/index.html", {'form': form, 'message': message})



def basket(request, client_id):
    products = []
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(client=client).all()
    for order in orders:
        products.append(order.product.all())
    products.reverse()
    return render(request, 'store_app/all_orders.html', {'user': client, 'orders': orders, 'products': products})


def sorted_basket(request, client_id, days_ago):
    products = []
    product_set = []
    now = datetime.now()
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(client=client, order_date__gte=now - timedelta(days=days_ago))
    for order in orders:
        products = order.product.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)

    return render(request, 'store_app/all_products.html',
                  {'client': client, 'product_set': product_set, 'days': days_ago})
