from django.urls import path
from .views import get_set, create_set

urlpatterns = [
    path('get_set',get_set),
    path('create_set',create_set)
    
]