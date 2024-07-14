from django.urls import path
from carts.views import *

urlpatterns = [
   
    path('', CartItemList.as_view()),
    path('item/<int:item_id>/', CartItemDetail.as_view())
]