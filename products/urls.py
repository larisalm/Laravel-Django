""" from django.urls import path
from .views import ProductList, ProductDetail

urlpatterns =[
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<init:pk', ProductDetail.as_view(), name='product-detail'),
] """

from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', ProductViewSet, basename = 'products' )
router.register('categories', CategoryViewSet, basename = 'categories')


urlpatterns = [
    path('', include(router.urls))
]
