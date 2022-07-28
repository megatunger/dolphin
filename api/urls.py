from . import views
from django.urls import path

urlpatterns = [
    path('v1/scalar/account', views.account, name='account'),
    path('v1/scalar/register', views.register, name='register'),
]
