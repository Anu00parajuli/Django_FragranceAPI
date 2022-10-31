import uuid

from django.contrib.auth.models import User
from rest_framework import (
    generics,
    permissions,
    status,
)
from rest_framework.response import Response

from .models import (
    Brand,
    Cart,
    Fragrance,
)
from .serializers import (
    BrandSerializer,
    CartSerializer,
    FragranceSerializer,
    RegistrationSerializer,
    UserSerializer,
)


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response({"Errors": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(
            {
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                "User": serializer.data
            },
            status=status.HTTP_201_CREATED)


class ListBrand(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class DetailBrand(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ListFragrance(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Fragrance.objects.all()
    serializer_class = FragranceSerializer


class DetailFragrance(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Fragrance.objects.all()
    serializer_class = FragranceSerializer


class ListUser(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListCart(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
