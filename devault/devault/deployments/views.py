from devault.deployments.models import Deployment
from rest_framework import viewsets
from devault.deployments.serializers import DeploymentSerializer

class DeploymentViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows environments to be viewed.
    """
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer
