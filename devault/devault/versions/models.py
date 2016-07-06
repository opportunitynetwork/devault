from django.db import models
from devault.users.models import CommonInfo, NameMixIn

class Version(CommonInfo, NameMixIn):
    pass
