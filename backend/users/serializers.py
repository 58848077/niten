import datetime
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.hashers import (
    make_password, 
    check_password,
)
from rest_framework import serializers, exceptions

from users.models import Room

User = get_user_model()

class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "name",
            "password",
        )
    
    def validate(self, attrs):
        return attrs
    
    def create(self, validated_data):
        request_data = Room.objects.create(
            name=validated_data["name"],
            password=make_password(validated_data["password"]),
            )
        request_data.save()
        
        return request_data
    
class RoomNameUpdateSerializer(serializers.ModelSerializer):
    model = Room
    fields = (
        "name",
    )
    
class RoomPasswordUpdateSerializer(serializers.ModelSerializer):
    model = Room
    fields = (
        "password",
    )
    def validate(self, attrs):
        return attrs
    
    def update(self, instance, validated_data):
        if check_password(validated_data.get["origin_password"], self.password):
            instance.password = make_password(validated_data.get["password"])
            instance.save()
            return instance
        return False