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
        cart_items = cart.cartItems.all()
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)
    
    def post(self, request): 
        cart = Cart.get_user_cart(request.user)
        food = Food.get_food_by_id(request.data['food'])
        
        cart_item, created = CartItem.objects.get_or_create(cart=cart, food=food)
        if not created:
            return Response({'error':'This item is already in the cart'}, status=status.HTTP_400_BAD_REQUEST)
       
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# 여행 장바구니에 조회 및 삭제
class CartItemDetail(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, item_id):
        user = request.user
        cart = Cart.get_user_cart(user)
        cart_item = get_object_or_404(cart.cartItems, id=item_id)
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)
        

    def delete(self, request, item_id):
        user = request.user
        cart = Cart.get_user_cart(user)
        cart_item = get_object_or_404(cart.cartItems, id=item_id)
        cart_item.delete()
        return Response(status.HTTP_204_NO_CONTENT)