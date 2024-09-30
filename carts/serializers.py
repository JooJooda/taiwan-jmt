from rest_framework import serializers
from .models import *
from foods.serializers import *

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"

class CartFoodSerializer(serializers.ModelSerializer):
    food = FoodSerializer()

    class Meta:
        model = CartFood
        fields = "__all__"