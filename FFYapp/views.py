from .models import Brand, Fragrance, Product , Cart
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegistrationSerializer, BrandSerializer, FragranceSerializer, ProductSerializer, CartSerializer, UserSerializer
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
import uuid

class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    def post(self,request):
        serializer = self.get_serializer(data = request.data)

        if (serializer.is_valid()):
            serializer.save()
        return Response({
            "RequestId": str(uuid.uuid4()),
            "Message": "User created successfully",

            "User": serializer.data}, status=status.HTTP_201_CREATED
        )

        return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)



class ListBrand(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class DetailBrand(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ListFragrance(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset = Fragrance.objects.all()
    serializer_class = FragranceSerializer

class DetailFragrance(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Fragrance.objects.all()
    serializer_class = FragranceSerializer

class ListProduct(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListUser(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListCart(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer




