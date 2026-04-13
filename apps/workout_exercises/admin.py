from django.contrib import admin

from ..workout_exercises.models import Workout_Exercises
from ..sets.models import Sets

class SetInline(admin.TabularInline):
    model = Sets
    extra = 1    
    
@admin.register(Workout_Exercises)
class WorkOutExercisesAdmin(admin.ModelAdmin):
    list_display = ('workout_exercise_id','workout','exercise')
    search_fields = (['workout'])
    inlines = [SetInline]