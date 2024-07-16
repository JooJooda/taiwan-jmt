from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.permissions import *

class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user = get_object_or_404(User, id=user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
        
