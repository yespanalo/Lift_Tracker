from rest_framework import serializers
from .models import Workout_Exercises
from ..sets.serializers import SetsSerializer

class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise_name = serializers.CharField(source='exercise.name')
    sets = SetsSerializer(many=True,read_only=True)

    class Meta:
        model = Workout_Exercises
        fields = ['workout_exercise_id', 'exercise', 'exercise_name','sets']