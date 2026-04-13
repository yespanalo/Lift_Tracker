from django.contrib import admin

from ..exercise.models import Exercise
from ..sets.models import Sets
from ..workout_exercises.models import Workout_Exercises
from ..workouts.models import Workout


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise_id','name','muscle_group','created_by','created_at')
    search_fields = (['name'])
    list_filter = (['muscle_group'])