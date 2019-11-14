from django.urls import include, path
from rest_framework import routers
from catchup import api as catchup_api

router = routers.DefaultRouter()
router.register(r'event', catchup_api.EventViewSet)
router.register(r'groups', catchup_api.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
