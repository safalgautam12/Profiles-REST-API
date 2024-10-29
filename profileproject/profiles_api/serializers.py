from rest_framework import serializers

from profiles_api import models

#it also validates the content 
class HelloSerializer(serializers.Serializer):
    """Serializes the name filed for testing our APIView"""
    name=serializers.CharField(max_length=10) 
    


#model serializer has more features as compared to normal serializer 


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a user profile object """
    
    
    class Meta:
        model=models.UserProfile
        #list of fields that we want to manage through serializers
        fields= ('id','email','name','password')
        #making password field write only
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
        
    def create(self,validated_data):
        """Create and return a new user"""
        user =models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            
        )
        
        return user
