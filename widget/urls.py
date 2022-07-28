from . import views
from django.urls import path

urlpatterns = [
    path('generic', views.generic, name='home'),
]
