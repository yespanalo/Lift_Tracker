from django.urls import path
from .views import get_workouts, create_workout, create_workout_with_exercises

urlpatterns = [
    path('get_workouts',get_workouts),
    path('create_workout',create_workout),
    path('create_workout_with_exercises',create_workout_with_exercises)
]
