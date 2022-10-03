from rest_framework.routers import DefaultRouter
from .views import StudentClassViewSet

router = DefaultRouter()

router.register(r'student_class', StudentClassViewSet, basename='student_class')

urlpatterns = router.urls