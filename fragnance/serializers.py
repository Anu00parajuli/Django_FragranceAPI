from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import (
    Brand,
    Cart,
    Fragrance,
)


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

        @staticmethod
        def validate(args):
            email = args.get('email', None)
            username = args.get('username', None)

            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    {'email': _('Email already exists')})
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError(
                    {'username': _('username already exists')})
            return args

        @staticmethod
        def create(validated_data):
            return User.objects.create_user(**validated_data)


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
            'imageUrl',
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
