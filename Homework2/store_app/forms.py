import datetime

from django import forms


class ProductsForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название')
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Описание  продукта'}), label='Описание')
    price = forms.DecimalField(max_digits=8, decimal_places=2, label='Цена')
    quantity = forms.IntegerField(label='Количество')
    date_added = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Дата добавления', initial=datetime.date.today())
    image = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Изображение продукта'}), required=False, label='Изображение')



