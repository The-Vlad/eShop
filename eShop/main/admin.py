from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(Order)
