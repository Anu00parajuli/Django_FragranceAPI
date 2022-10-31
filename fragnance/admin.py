from django.contrib import admin

from .models import (
    Brand,
    Cart,
    Fragrance,
    Product,
)

admin.site.register(Brand)
admin.site.register(Fragrance)
admin.site.register(Product)
admin.site.register(Cart)

# Register your models here.
