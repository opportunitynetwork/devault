from devault.environments.models import Environment
from rest_framework import viewsets
from devault.environments.serializers import EnvironmentSerializer
from rest_framework import generics
from rest_framework import mixins
class EnvironmentViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows environments to be viewed.
    """
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    
class EnvironmentList(generics.RetrieveAPIView):
    serializer_class = EnvironmentSerializer

    def get_object(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        name = self.kwargs['name']
        return Environment.objects.get(name=name)