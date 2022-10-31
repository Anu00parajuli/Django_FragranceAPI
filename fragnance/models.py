from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Brand(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title


class Fragrance(models.Model):
    title = models.CharField(max_length=150)
    brand = models.ForeignKey(Brand,
                              related_name='fragrances',
                              on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    fragrances = models.ManyToManyField(Fragrance)

    class Meta:
        ordering = ['-created_at']

    def save(self,
             force_insert=False,
             force_update=False,
             using=None,
             update_fields=None):
        if not Cart.objects.filter(user=self.user).exists():
            return super().save(force_insert, force_update, using,
                                update_fields)
        cart = Cart.objects.get(user=self.user)
        cart.fragrances.add(*self.fragrances.all())
        return cart
