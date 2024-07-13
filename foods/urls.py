from django.urls import path
from foods.views import *

urlpatterns = [
   
    path('', FoodList.as_view()),
    path('<int:id>/', FoodDetail.as_view()),
]