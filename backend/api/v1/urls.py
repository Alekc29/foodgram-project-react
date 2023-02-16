
from django.urls import include, path
from rest_framework.routers import DefaultRouter


app_name = 'api.v1'

router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls), name='api-root'),
    
]
