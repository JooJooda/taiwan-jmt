from django.db import models
from foods.models import Food
from accounts.models import User
from rest_framework.response import Response
from rest_framework import status

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, related_name="cart", on_delete=models.CASCADE)

    def get_user_cart(user):
        try:
            return Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def create_cart(user):
        cart = Cart.objects.create(user=user)
        cart.save()
        return cart
        
class CartFood(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, related_name="cartFoods", on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name="cartFoods", on_delete=models.CASCADE)
