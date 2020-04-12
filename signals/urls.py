from django.urls import path,include
from .views import home, Api,details
from rest_framework import routers

router = routers.DefaultRouter()
router.register('signal', Api)

urlpatterns = [
    path('', home, name="home"),
    path('details/<id>', details, name="details"),
    path('api-auth', include('rest_framework.urls', namespace="rest_framework")),
    path('api/', include(router.urls)),
]
