from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)  # ✅ no basename needed if queryset is defined

urlpatterns = [
    path('', include(router.urls)),
]