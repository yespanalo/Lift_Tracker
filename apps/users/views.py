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
    