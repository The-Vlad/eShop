from .models import *
from django.forms import ModelForm, TextInput, Textarea


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["id_employee", "full_name", "inn", "phone_number", "id_auth_user"]
        widgets = {
            "full_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите полное имя'
            }),
            "inn": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите ИНН сотрудника'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона'
            })
        }

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["id_client", "full_name", "phone_number", "email", "bonuses", "id_auth_user"]
        widgets = {
            "full_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите полное имя'
            }),
            "phone_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона'
            }),
            "email": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите адрес электронной почты'
            }),
            "bonuses": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество бонусов'
            })
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["id_product", "name", "cost", "description", "quantity", "id_employee"]
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
            }),
            "id_employee": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ID сотрудника'
            })
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["id_review", "datetime", "text", "id_client", "id_product"]
        widgets = {
            "datetime": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату и время публикации  (YYYY-MM-DD hh:mm:ss)'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст отзыва'
            }),
            "id_client": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ID клиента'
            }),
            "id_product": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ID товара'
            })
        }

class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ["id_cart", "id_product"]
        widgets = {
            "id_product": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ID товара'
            })
        }

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["id_order", "total_cost", "delivery", "datetime", "receipt",
                  "id_cart", "id_client"]
        widgets = {
            "total_cost": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите итоговую стоимость'
            }),
            "delivery": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес доставки'
            }),
            "datetime": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату и время (YYYY-MM-DD hh:mm:ss)'
            }),
            "receipt": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите квитанцию'
            }),
            "id_cart": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ID корзины'
            }),
            "id_client": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ID клиента'
            })
        }