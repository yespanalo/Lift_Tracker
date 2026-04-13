from django.db import models
from ..workout_exercises.models import Workout_Exercises

class Sets(models.Model):
    set_id = models.AutoField(primary_key=True)
    workout_exercise_id = models.ForeignKey(
        Workout_Exercises,
        on_delete=models.CASCADE,
        related_name= 'sets',null=True, blank=True
    )
    set_number = models.IntegerField(null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    weight_in_pounds = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Set {self.set_number} - {self.reps} reps @ {self.weight_in_pounds}lbs"