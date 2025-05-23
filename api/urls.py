from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RideViewSet, RegisterUserView

router = DefaultRouter()
router.register('rides', RideViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUserView.as_view(), name='register'),
]
