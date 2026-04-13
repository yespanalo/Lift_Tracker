from django.contrib import admin

from ..workouts.models import Workout
from ..workout_exercises.models import Workout_Exercises

class WorkoutExerciseInline(admin.TabularInline):
    model = Workout_Exercises
    extra = 1

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('workout_id','user','workout_date','notes','created_at')
    search_fields=(['user__user_name'])
    inlines = [WorkoutExerciseInline]