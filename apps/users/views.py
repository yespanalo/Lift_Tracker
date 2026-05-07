from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from .serializers import RegisterSerializer, CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser


@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"success":True,"message":"User created"},status= status.HTTP_201_CREATED)
    
    return Response({"success":False, "message":serializer.errors}, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(email=email,password = password)
    
    if user is None:
        return Response({"success":False,"message":"Invalid credentials"},status= status.HTTP_401_UNAUTHORIZED)
    
    refresh = RefreshToken.for_user(user)
    
    
    return Response({"success":True,"access":str(refresh.access_token),"refresh":str(refresh),"message":CustomUserSerializer(user).data},status= status.HTTP_200_OK)

@api_view(['GET'])
def get_users(request):
    user = CustomUser.objects.all()
    serializer = CustomUserSerializer(user,many = True)
    return Response({"success":True,"message":serializer.data})

from datetime import datetime, timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def format_json(request):
    start_time = request.data.get('start_time')
    end_time = request.data.get('end_time')

    includes = request.data.get('includes')
    excludes = request.data.get('excludes')

    # Validate required fields
    if not start_time or not end_time:
        return Response(
            {"error": "start_time and end_time are required"},
            status=400
        )

    # Default to empty lists if not provided
    if includes is None:
        includes = []

    if excludes is None:
        excludes = []

    result = {
        "start_time": start_time,
        "end_time": end_time,
        "includes": includes,
        "excludes": excludes
    }

    return Response(result)

@api_view(['POST'])
def create_config(request):
    duration_seconds = request.data.get('duration_seconds')
    lead_time_seconds = request.data.get('lead_time_seconds')
    requires_approval = request.data.get('requires_approval')
    interval_mmCss_csv = request.data.get('interval_mmCss_csv')
    
    if not duration_seconds or not lead_time_seconds or not interval_mmCss_csv:
        return Response({"error":"duration_seconds,lead_time_seconds and interval_mmCss_csv are required"})
    
    result = {
        "duration_seconds":duration_seconds,
        "lead_time_seconds":lead_time_seconds,
        "requires_approval":requires_approval,
        "interval_mmCss_csv":interval_mmCss_csv
    }
    
    return Response(result)