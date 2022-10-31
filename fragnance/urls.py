from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'brands', views.BrandViewSet)
router.register(r'carts', views.CartViewSet)
router.register('', views.FraganceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
