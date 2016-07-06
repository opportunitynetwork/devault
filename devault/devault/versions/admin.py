from django.contrib import admin
from devault.users.mixins import AdminMixIn,AdminMixInName
from devault.versions.models import Version

class VersionAdmin(AdminMixInName, AdminMixIn):
    pass
admin.site.register(Version, VersionAdmin)
