from django.contrib import admin
from devault.deployments.models import Deployment
from devault.users.mixins import AdminMixIn

class DeploymentAdmin(AdminMixIn):
    list_display = ("version", "environment", "author", "created", "editor", "modified")
    fields = ('version', 'environment')
admin.site.register(Deployment, DeploymentAdmin)
    