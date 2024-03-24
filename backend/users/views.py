# from email import header
from logging import warning
import requests, os
from dotenv import load_dotenv

from django.contrib.auth import get_user_model
from django.conf import settings
from datetime import datetime
from django.template.loader import render_to_string  
from django.core.mail import EmailMessage,send_mail
from django.contrib.sessions.models import Session 
from django.utils import timezone
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, token_verify

from users.models import (
    Room, 
    RoomUser, 
    UserPermission,
)

User = get_user_model()
load_dotenv()

class RoomView(APIView):
    def get(self, request, format=None):
        pass
    
    def post(self, request, format=None):
        pass
    
class RoomDetailView(APIView):
    def get(self, request, id, format=None):
        pass
    
    def put(self, request, id, format=None):
        pass
    
    def delete(self, request, id, format=None):
        pass
    
class UserView(APIView):
    def get(self, request, format=None):
        pass
    
    def post(self, request, format=None):
        pass
    
class UserDetailView(APIView):
    def get(self, request, id, format=None):
        pass
    
    def put(self, request, id, format=None):
        pass
    
    def delete(self, request, id, format=None):
        pass
    
    