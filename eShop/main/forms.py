from .models import Product
from django.forms import ModelForm, TextInput, Textarea


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "cost", "description", "quantity"]
        widgets = {
            "name": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите название'
            }),
            "cost": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите стоимость'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "quantity": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество'
            })
        }