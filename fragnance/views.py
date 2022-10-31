from rest_framework import (
    permissions,
)
from rest_framework.viewsets import ModelViewSet

from .models import (
    Brand,
    Cart,
    Fragrance,
)
from .serializers import (
    BrandSerializer,
    CartSerializer,
    FragranceSerializer,
)


class BrandViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class FraganceViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Fragrance.objects.all()
    serializer_class = FragranceSerializer


class CartViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
