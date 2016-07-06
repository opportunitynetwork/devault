from devault.versions.models import Version
from rest_framework import viewsets
from devault.versions.serializers import VersionSerializer

class VersionViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows versions to be viewed.
    """
    queryset = Version.objects.all()
    serializer_class = VersionSerializer


