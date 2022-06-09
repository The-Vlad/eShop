from django.db import models


# Create your models here.
class Employee(models.Model):
    id_employee = models.IntegerField('ID сотрудника', primary_key=True)
    full_name = models.CharField("Полное имя", max_length=45)
    inn = models.CharField("ИНН сотрудника", max_length=45, unique=True)
    phone_number = models.CharField("Номер телефона", max_length=20, null=True)
    id_auth_user = models.IntegerField("ID пользователя")

    class Meta:
        db_table = 'employee'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.full_name


class Client(models.Model):
    id_client = models.IntegerField('ID клиента', primary_key=True)
    full_name = models.CharField("Полное имя", max_length=45)
    phone_number = models.CharField("Номер телефона", max_length=20)
    email = models.CharField("Адрес электронной почты", max_length=45)
    bonuses = models.IntegerField("Количество бонусов")
    id_auth_user = models.IntegerField("ID пользователя")

    class Meta:
        db_table = 'client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.full_name


class Product(models.Model):
    id_product = models.IntegerField('ID товара', primary_key=True)
    name = models.CharField('Название', max_length=45)
    cost = models.FloatField('Цена')#, default=0)
    description = models.TextField('Описание', default='')
    quantity = models.IntegerField('Количество')#, default=0)
    id_employee = models.IntegerField("ID сотрудника")

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

class Review(models.Model):
    id_review = models.IntegerField('ID отзыва', primary_key=True)
    datetime = models.DateTimeField('Дата и время')
    text = models.TextField('Текст отзыва', null=True)
    id_client = models.IntegerField('ID клиента')
    id_product = models.IntegerField('ID товара')

    class Meta:
        db_table = 'review'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.id_review

class Cart(models.Model):
    id_cart = models.IntegerField('ID корзины')
    id_product = models.IntegerField('ID товара')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return self.id_cart

class Order(models.Model):
    id_order = models.IntegerField('ID заказа', primary_key=True)
    total_cost = models.FloatField("Итоговая стоимость")
    delivery = models.CharField('Адрес доставки', max_length=45)
    datetime = models.DateTimeField('Дата и время')
    receipt = models.TextField("Квитанция")
    id_cart = models.IntegerField('ID корзины')
    id_client = models.IntegerField('ID клиента')

    class Meta:
        db_table = 'eshop.order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.id_order