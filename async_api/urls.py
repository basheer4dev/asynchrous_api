from django.urls import path

from .views import home, call_first_endpoint, call_second_endpoint

urlpatterns = [
    path('', home, name='home'),
    path('call_first_endpoint/', call_first_endpoint, name='first'),
    path('call_second_endpiont/', call_second_endpoint, name='second'),
]