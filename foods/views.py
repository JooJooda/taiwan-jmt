from django.shortcuts import render
from .serializers import FoodSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Food
from django.shortcuts import get_object_or_404


# 쿼리 파라미터를 사용하여 분기 처리
class FoodList(APIView):
    def get(self, request):

        category = request.query_params.get('category', None)
        recommend = request.query_params.get('recommend', None)

        food = Food.objects.all()

        if category :
            food = food.filter(category=category)

        if recommend :
            food = food.filter(is_recommendation=recommend)  

        serializer = FoodSerializer(food, many=True)
        return Response(serializer.data)

class FoodDetail(APIView):
    def get(self, request, id):
        food = get_object_or_404(Food, id=id)
        serializer = FoodSerializer(food)
        return Response(serializer.data)