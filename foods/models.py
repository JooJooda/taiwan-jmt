from django.db import models
from rest_framework.response import Response
from rest_framework import status

class Food(models.Model):

    CHOICES = (
        ('MEAL', '식사'),
        ('DESSERT', '디저트'),
        ('DRINK', '음료'),
        ('NIGHTMARKET', '야시장'),
        ('ETC', '기타'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="이름", max_length=20)
    description = models.CharField(verbose_name="설명", max_length=200, null=True, blank=True)
    recommend_menu = models.CharField(verbose_name="추천메뉴", max_length=100)
    google_map_addr = models.CharField(verbose_name="구글맵주소", max_length=200)
    tip = models.CharField(verbose_name="꿀팁", max_length=100, null=True, blank=True)
    is_recommendation = models.BooleanField(verbose_name="추천항목여부", default=False)
    category = models.CharField(choices=CHOICES, max_length=11)

    def get_food_by_id(id):
        try: 
            return Food.objects.get(id=id)
        except Food.DoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)


class Thumbnail(models.Model):
    id = models.AutoField(primary_key=True)
    food = models.ForeignKey(Food, related_name="thumbnails", on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name="썸네일")