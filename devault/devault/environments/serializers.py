from devault.environments.models import Environment
from rest_framework import serializers


class EnvironmentSerializer(serializers.HyperlinkedModelSerializer):
    tier = serializers.CharField(source='get_tier_display')
    class Meta:
        model = Environment
        fields = ('id', 'name', 'current_version','tier','created', 'modified')


