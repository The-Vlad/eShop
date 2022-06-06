from django.db import models

# Create your models here.

class Role(models.Model):
    id = models.IntegerField('ID продукта', primary_key=True)
    name = models.CharField('Название', max_length=45)
    cost = models.FloatField('Цена')#, default=0)
    description = models.TextField('Описание', default='')
    quantity = models.IntegerField('Количество')#, default=0)

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.IntegerField('ID продукта', primary_key=True)
    name = models.CharField('Название', max_length=45)
    cost = models.FloatField('Цена')#, default=0)
    description = models.TextField('Описание', default='')
    quantity = models.IntegerField('Количество')#, default=0)

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

