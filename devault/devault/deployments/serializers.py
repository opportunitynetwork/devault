from devault.deployments.models import Deployment
from rest_framework import serializers

class DeploymentSerializer(serializers.HyperlinkedModelSerializer):
    version = serializers.StringRelatedField(many=False)
    environment = serializers.StringRelatedField(many=False)
    author = serializers.StringRelatedField(many=False)
    editor = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Deployment
        fields = ('version','environment', 'author', 'created', 'editor', 'modified')
