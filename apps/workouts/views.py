from .models import Workout
from ..workout_exercises.models import Workout_Exercises
from .serializers import WorkoutSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_workouts(request):
    try:
        date_filter = request.GET.get('workout_date',None)
        workouts = Workout.objects.filter(user=request.user).prefetch_related('workout_exercises__exercise',
        'workout_exercises__sets')
        if date_filter:
            workouts = workouts.filter(workout_date=date_filter)
        serializer = WorkoutSerializer(workouts, many = True)
        return Response({"success":True,"data":serializer.data})
    except Exception as e:
        return Response({"success": False,"message":str(e)})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_workout(request):
    try:
        serializer = WorkoutSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response({"success":True,"data":serializer.data})
    except Exception as e:
        return Response({"success":False,"message":str(e)})
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_workout_with_exercises(request):
    try:
        workout_date = request.data.get('workout_date')
        exercise_data = request.data.get('exercises',[])
        notes = request.data.get('notes', '')
        
        if not workout_date:
            return Response({"success":False,"message":"Workout date is required"})
            
        with transaction.atomic():
            workout, created = Workout.objects.get_or_create(
                user = request.user,
                workout_date = workout_date,
                defaults={
                    'notes':notes
                }
            )
            
            if not created and notes:
                workout.notes = notes
                workout.save()

            for exercise_data in exercise_data:
                exercise_id = exercise_data.get('exercise_id')
                
                workout_exercise = Workout_Exercises.objects.create(
                    workout = workout,
                    exercise_id = exercise_id
                )
            
            workout.refresh_from_db()
            serializer = WorkoutSerializer(workout)
            
            return Response({"success": True,"data":serializer.data,"create_or_append":"create" if created else"append"})
                
        
    except Exception as e:
        return Response({"success":False,"message":str(e)})
    