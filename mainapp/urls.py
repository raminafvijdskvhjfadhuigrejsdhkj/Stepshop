

from django.urls import path
from .views import index, products, product, about, contacts



urlpatterns = [
    path('', index),

]
urlpatterns = [
    path('', index),
    path('products/', products),
]

urlpatterns = [
    path('', index),
    path('product/', product),
]

urlpatterns = [
    path('', index),
    path('about/', about),
]

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
]
