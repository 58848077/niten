import uuid
from django.db import models
from django.contrib.auth.hashers import (
    make_password, 
    check_password,
)
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager, 
)

class UserPermission(models.Model):
    permission_choices = (
        ("developer", "developer"),
        ("superuser", "superuser"),
        ("user", "user"),
    )
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50, choices=permission_choices, default=permission_choices[0][0], unique=True)
    
    def __str__(self):
        return f"{self.id}, {self.name}"
    
class Room(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    creator = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    member = models.ManyToManyField("User", through='RoomUser', through_fields=('room', 'user'))
    
    is_archived = models.BooleanField(default=False)
    
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} {'(已封存)' if self.is_archived else ''}"
    
    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)
    #     self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
class User(AbstractBaseUser):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25, unique=True)
    email = models.EmailField(verbose_name='Email Address', max_length=255, unique=True)
    password = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    
    permission = models.ForeignKey(UserPermission, on_delete=models.SET_NULL, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id}, {self.name} {'(非活躍)' if not self.is_active else ''}"
    
    @property
    def developer_perm(self):
        return self.permission.name == "developer"
    
    @property
    def superuser_perm(self):
        perms = ["superuser", "developer"]
        return self.permission.name in perms
    
class RoomUser(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    join_time = models.DateTimeField(auto_now_add=True)
    leave_time = models.DateTimeField()
    
    def __str__(self):
        return f"{self.room.name} 的使用者: {self.user.name}"
    