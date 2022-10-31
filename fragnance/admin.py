from django.contrib import admin

from .models import (
    Brand,
    Cart,
    Fragrance,
)

admin.site.register(Brand)
admin.site.register(Fragrance)
admin.site.register(Cart)
