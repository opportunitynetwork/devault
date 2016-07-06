from django.contrib.auth.models import User
from django.db import models

from devault.users.models import CommonInfo
from devault.versions.models import Version
from devault.environments.models import Environment

class Deployment(CommonInfo):
    version = models.ForeignKey(Version)
    environment = models.ForeignKey(Environment)
    def __str__(self):
        return '%s @ %s' % (self.version, self.environment)
