from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class DevOp(models.Model):
    """User profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    

class CommonInfo(models.Model):
    """Abstract class with common fields.
    """
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, related_name="%(app_label)s_%(class)s_related_author")
    editor = models.ForeignKey(User, null=True, related_name="%(app_label)s_%(class)s_related_editor")

    class Meta:
        abstract = True
        ordering = ["-created"]
        get_latest_by = "created"

class NameMixIn(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)