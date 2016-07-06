from devault.versions.models import Version
from rest_framework import serializers

class VersionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Version
        fields = ('name', 'created', 'modified')
