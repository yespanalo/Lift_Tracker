from .models import Sets
from .serializers import SetsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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