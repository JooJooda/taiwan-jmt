from rest_framework import serializers
from .models import *
from carts.models import *
from carts.serializers import *
from rest_framework_simplejwt.serializers import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['username','email', 'cart']

class OAuthSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email']
    
    def validate(self, data):
        email = data.get('email', None)
        username = data.get('name', None)

        if email is None:
            raise serializers.ValidationError('Email does not exist.')
        
        if username is None:
            username = email.split('@')[0]

        user = User.get_user_by_email(email=email)
        
        if user is None:
            user = User.objects.create(email=email, username=username)
            Cart.create_cart(user=user)
            user.save()
        
        token = RefreshToken.for_user(user)
        refresh_token = str(token)
        access_token = str(token.access_token)

        data = {
            "user": user,
            "refresh_token": refresh_token,
            "access_token": access_token,
        }

        return data