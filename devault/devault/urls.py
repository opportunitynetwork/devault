from django.conf.urls import url, include
from rest_framework import routers
from devault.environments.views import EnvironmentViewSet, EnvironmentList
from devault.versions.views import VersionViewSet
from devault.deployments.views import DeploymentViewSet
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),    
    url(r'^$', login_required(TemplateView.as_view(template_name="frontend/index.html"))),
    url(r'^admin/', include(admin.site.urls)),
    url('^environments/(?P<name>[a-z0-9A-Z].+)/$', EnvironmentList.as_view()),
    
]


router = routers.DefaultRouter()
router.register(r'environments', EnvironmentViewSet)
router.register(r'versions', VersionViewSet)
router.register(r'deployments', DeploymentViewSet)

urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

