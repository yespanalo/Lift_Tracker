from django.urls import path
from .views import get_exercises,create_exercise

urlpatterns = [
    path('get_exercises', get_exercises),
    path('create_exercise', create_exercise)
]
