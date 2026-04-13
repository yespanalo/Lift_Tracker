from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_name','email','password','gender']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self,validate_data):
        return CustomUser.objects.create_user(**validate_data)
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_id','user_name','email','gender']