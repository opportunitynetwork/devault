from django.contrib import admin
from devault.users.mixins import AdminMixIn,AdminMixInName
from devault.environments.models import Environment

class EnvironmentAdmin(AdminMixInName, AdminMixIn):
    fields = ("name", "tier", "comment")
    list_display = ("name", "tier", "author", "created", "editor", "modified")
    
    pass
admin.site.register(Environment, EnvironmentAdmin)


