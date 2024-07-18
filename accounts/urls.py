from django.urls import path
from .views import *

urlpatterns = [
   
    path('', UserDetail.as_view()),
    path("google/login/", google_login, name="google_login"),
    path("google/callback/", google_callback, name="google_callback"),
]