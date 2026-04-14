from rest_framework import serializers
from .models import Sets

class SetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sets
        fields = ['set_id','workout_exercise_id', 'set_number', 'reps', 'weight_in_pounds']