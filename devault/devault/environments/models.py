from django.db import models
from devault.users.models import CommonInfo, NameMixIn

TIER_CHOICES = (
    (0, 'Development'),
    (1, 'Integration'),
    (2, 'Testing'),
    (3, 'Staging'),
    (4, 'Production')
)

class Environment(CommonInfo, NameMixIn):
    tier = models.IntegerField(choices=TIER_CHOICES)
    @property
    def current_version(self):
        return self.deployment_set.latest().version.name
