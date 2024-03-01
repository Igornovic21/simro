from django.contrib import admin

from product.models import Product, Marque

# Register your models here.
admin.site.register(Marque)
admin.site.register(Product)