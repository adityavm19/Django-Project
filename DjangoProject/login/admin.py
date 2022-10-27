from django.contrib import admin
from login.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','email', 'first_name','last_name','username','mobile','accType', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Users Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name','mobile','accType','last_name','username')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','mobile','accType', 'password1', 'password2','username','last_name'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.


# Register your models here.
