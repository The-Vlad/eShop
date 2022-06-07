from .models import *
from django.forms import ModelForm, TextInput, Textarea


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["id", "username", "password", "last_login", "date_joined",
                  "first_name", "last_name", "email", "phone_number", "bonuses",
                  "is_active", "is_staff", "is_superuser"]
        widgets = {
            "username": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите имя пользователя'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }),
            "first_name": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес электронной почты'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона'
            }),
            "bonuses": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество бонусов'
            }),
            "is_active": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите статус активности'
            }),
            "is_staff": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите статус сотрудника'
            }),
            "is_superuser": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите статус суперпользователя'
            })
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["id_product", "name", "cost", "description", "quantity"]
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

