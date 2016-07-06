from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from devault.users.models import DevOp

class DevOpInline(admin.StackedInline):
    model = DevOp
    can_delete = False
    verbose_name_plural = 'devops'

class TokenInline(admin.StackedInline):
    model = Token
    can_delete = False
    verbose_name_plural = 'tokens'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (DevOpInline, TokenInline)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)