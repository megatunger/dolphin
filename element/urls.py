from . import views
from django.urls import path

urlpatterns = [
    path('', views.ElementList.as_view(), name='home'),
]
