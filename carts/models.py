from django.db import models
from foods.models import Food
from accounts.models import User


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, related_name="cart", on_delete=models.CASCADE)

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, related_name="cartItems", on_delete=models.CASCADE)
    food = models.ForeignKey(Food, related_name="cartItems", on_delete=models.CASCADE)
