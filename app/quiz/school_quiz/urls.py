from rest_framework.routers import DefaultRouter
from .views import StudentClassViewSet, StudentViewSet, ClassTestViewSet, StudentScoreViewSet

router = DefaultRouter()

router.register(r'student', StudentViewSet, basename='student')
router.register(r'student_class', StudentClassViewSet, basename='student_class')
router.register(r'test', ClassTestViewSet, basename='test')
router.register(r'score', StudentScoreViewSet, basename='score')

urlpatterns = router.urls