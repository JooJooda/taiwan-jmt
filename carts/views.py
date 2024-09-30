from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.permissions import *


# 여행 장바구니 조회 및 추가
class CartItemList(APIView):
   
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        cart = Cart.get_user_cart(user)
        # 역참조
        cart_foods = cart.cartFoods.all()
        serializer = CartFoodSerializer(cart_foods, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        #print(request.user) 
        cart = Cart.get_user_cart(request.user)
        food = Food.get_food_by_id(request.data['food'])
        
        cart_foods, created = CartFood.objects.get_or_create(cart=cart, food=food)
        if not created:
            return Response({'error':'This item is already in the cart'}, status=status.HTTP_400_BAD_REQUEST)
       
        serializer = CartFoodSerializer(cart_foods)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# 여행 장바구니에 조회 및 삭제
class CartItemDetail(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, item_id):
        user = request.user
        cart = Cart.get_user_cart(user)
        cart_foods = get_object_or_404(cart.cartFoods, id=item_id)
        serializer = CartFoodSerializer(cart_foods)
        return Response(serializer.data)
        

    def delete(self, request, item_id):
        user = request.user
        cart = Cart.get_user_cart(user)
        cart_foods = get_object_or_404(cart.cartFoods, id=item_id)
        cart_foods.delete()
        return Response(status.HTTP_204_NO_CONTENT)