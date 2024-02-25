from django.contrib import admin
from .models import Products, Client, Order

# Register your models here.


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'date_added']
    ordering = ['-date_added']
    list_filter = ['date_added', 'price', 'quantity']
    search_fields = ['name']
    search_help_text = 'Поиск по названию продукта'
    fields = ['name', 'description', 'price', 'quantity', 'date_added', 'image']
    readonly_fields = ['date_added', 'image']
    save_on_top = True


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    ordering = ['name']
    list_filter = ['registration_date']
    search_fields = ['name']
    search_help_text = 'Поиск по имени клиента'
    readonly_fields = ['registration_date', 'name']
    save_on_top = True


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_sum', 'order_date']
    ordering = ['order_date']
    list_filter = ['order_date']
    search_fields = ['order_date']
    search_help_text = 'Поиск по дате заказа'
    readonly_fields = ['client', 'product','total_sum', 'order_date']
    save_on_top = True
