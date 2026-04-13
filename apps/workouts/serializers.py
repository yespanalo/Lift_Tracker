from rest_framework import serializers
from .models import Workout
from ..workout_exercises.serializers import WorkoutExerciseSerializer

class WorkoutSerializer(serializers.ModelSerializer):
    workout_exercises = WorkoutExerciseSerializer(many=True, read_only= True)
    
    class Meta:
        model = Workout
        fields = ['workout_id','user','workout_date','notes','created_at','workout_exercises']