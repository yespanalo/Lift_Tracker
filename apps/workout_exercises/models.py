from django.db import models
from apps.workouts.models import Workout
from apps.exercise.models import Exercise

class Workout_Exercises(models.Model):
    workout_exercise_id = models.AutoField(primary_key=True)
    
    workout = models.ForeignKey(
        Workout,
        on_delete=models.CASCADE,
        related_name= "workout_exercises"
    )
    
    exercise = models.ForeignKey(
        Exercise,
        on_delete= models.CASCADE,
        related_name= "exercise_workouts"
    )
    
    def __str__(self):
        return f"{self.workout} - {self.exercise}"