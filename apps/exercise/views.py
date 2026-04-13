from .models import Exercise
from .serializers import ExerciseSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_exercises(request):
    try:
        search_name = request.GET.get('name', None)
        filter_muscle_group = request.GET.get('group',None)
        
        exercise = Exercise.objects.all()
        
        if search_name:
            exercise = exercise.filter(name__icontains = search_name)
        
        if filter_muscle_group:
            exercise = exercise.filter(muscle_group__icontains = filter_muscle_group)
    
        serializer = ExerciseSerializer(exercise,many = True)
        return Response({"success":True,"data":serializer.data})
    except Exception as e:
        return Response({"success":False,"message":str(e)})
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_exercise(request):
    try:
        serializer = ExerciseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response({"success":True,"data":serializer.data})
    except Exception as e:
        return Response({"success":False,"message":str(e)})
