from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Brand,
    Cart,
    Fragrance,
)



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
        )
        model = Brand


class FragranceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'brand',
            'price',
            'stock',
            'description',
            'image',
            'status',
            'date_created',
        )
        model = Fragrance


class UserSerializer(serializers.ModelSerializer):
    fragrances = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Fragrance.objects.all())

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'fragrances',
        )


class CartUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class CartSerializer(serializers.ModelSerializer):
    cart_id = CartUserSerializer(read_only=True, many=True),
    fragrances = FragranceSerializer(read_only=True, many=True),

    class Meta:
        model = Cart,
        fields = (
            'card_id',
            'created_at',
            'fragrances',
            'products',
        )
