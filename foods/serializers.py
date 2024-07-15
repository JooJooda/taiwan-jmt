from rest_framework import serializers
from .models import *

class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = "__all__"

class FoodSerializer(serializers.ModelSerializer):
    # 역참조 필드 시리얼라이저
    thumbnails = ThumbnailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Food
        fields = "__all__"