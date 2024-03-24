from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import (
    UserPermission,
    Room,
    RoomUser,
)
from users.forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

# Remove Group Model from admin. We're not using it.

class CustomModelAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(CustomModelAdmin, self).__init__(model, admin_site)

class RoomAdmin(CustomModelAdmin):   
    pass

class UserPermissionAdmin(CustomModelAdmin):   
    pass

class RoomUserAdmin(CustomModelAdmin):   
    pass

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['name',  'email', 'desc', 'permission', 'is_active', 'is_staff', 'is_admin']
    list_filter = ['comp_id', 'admin']
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info', {'fields': ('permission', 'desc')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password','password_2')}
        ),
    )
    search_fields = ['email']
    ordering = ['email', 'name']
    filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(UserPermission, UserPermissionAdmin)
admin.site.register(RoomUser, RoomUserAdmin)
