from django.urls import path
from .views import get_set

urlpatterns = [
    path('get_set',get_set)
]