from django.urls import path

from .views import (
    DetailBrand,
    DetailFragrance,
    DetailUser,
    ListBrand,
    ListCart,
    ListFragrance,
    ListUser,
)

urlpatterns = [
    path('brands/', ListBrand.as_view(), name='brand'),
    path('brands/<int:pk>/', DetailBrand.as_view(), name='singlebrand'),
    path('fragrance/', ListFragrance.as_view(), name='fragrance'),
    path('fragrance/<int:pk>/',
         DetailFragrance.as_view(),
         name='singlefragrance'),
    path('users', ListUser.as_view(), name='user'),
    path('users/<int:pk>/', DetailUser.as_view(), name='singleuser'),
    path('carts/', ListCart.as_view(), name='cart'),
    path('carts/<int:pk>/', DetailUser.as_view(), name='singleuser')
]
