from .models import Sets
from .serializers import SetsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..workout_exercises.models import Workout_Exercises

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_set(request):
    try:
        workout_exercise_id = request.data.get('workout_exercise_id')
        
        set = Sets.objects.filter(
            workout_exercise_id__workout__user=request.user
        )
        
        if workout_exercise_id:
            set = set.filter(workout_exercise_id = workout_exercise_id)
            
        serializer = SetsSerializer(set, many = True)
        return Response ({"success":True, "data":serializer.data})
    except Exception as e:
        return Response ({"success":False,"message":str(e)})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_set(request):
    try:
        workout_exercise_id = request.data.get('workout_exercise_id')
        workout_exercise = Workout_Exercises.objects.get(
            pk=workout_exercise_id,
            workout__user=request.user
        )
        
        serializer = SetsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(workout_exercise_id=workout_exercise)
            return Response({"success":True, "data":serializer.data})
        return Response({"success":False,"message":serializer.errors})
    except Exception as e:
        return Response({"success":False,"message":str(e)})