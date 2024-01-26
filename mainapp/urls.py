

from django.urls import path
from .views import index, products, product, about, contacts

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('product/', product, name='product'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
]
