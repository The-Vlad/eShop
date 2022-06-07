from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField('ID Пользователя', primary_key=True)
    username = models.CharField("Имя пользователя", max_length=150)
    password = models.CharField("Пароль", max_length=128)
    last_login = models.DateTimeField("Последний вход", null=True)
    date_joined = models.DateTimeField("Дата регистрации")

    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    email = models.CharField("Адрес электронной почты", max_length=254)
    phone_number = models.CharField("Номер телефона", max_length=20, null=True)
    bonuses = models.IntegerField("Количество бонусов", null=True)

    is_active = models.BooleanField("Активный")
    is_staff = models.BooleanField("Статус персонала")
    is_superuser = models.BooleanField("Статус суперпользователя")

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username



class Product(models.Model):
    id_product = models.IntegerField('ID продукта', primary_key=True)
    name = models.CharField('Название', max_length=45)
    cost = models.FloatField('Цена')#, default=0)
    description = models.TextField('Описание', null=True)#, default='')
    quantity = models.IntegerField('Количество')#, default=0)

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
