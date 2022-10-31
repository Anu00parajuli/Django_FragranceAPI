from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Brand,
    Cart,
    Fragrance,
    Product,
)


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

        def validate(self, args):
            email = args.get('email', None)
            username = args.get('username', None)

            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    {'email': ('email already exists')})
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError(
                    {'username': ('username already exists')})

            return super().validate(args)

        def create(self, validated_data):
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


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'product_tag',
            'name',
            'brand',
            'price',
            'stock',
            'imageUrl',
            'status',
            'date_created',
        )
        model = Product


class UserSerializer(serializers.ModelSerializer):
    fragrances = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Fragrance.objects.all())
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'fragrances',
            'products',
        )


class CartUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class CartSerializer(serializers.ModelSerializer):
    cart_id = CartUserSerializer(read_only=True, many=True),
    fragrances = FragranceSerializer(read_only=True, many=True),
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Cart,
        fields = (
            'card_id',
            'created_at',
            'fragrances',
            'products',
        )


# class UserSerializer(serializers.ModelSerializer):
#     books = serializers.PrimaryKeyRelatedField(many=True, queryset=Fragrance.objects.all())
#     products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
#
#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'username',
#             'email',
#             'fragrances',
#             'products',
#         )
#
