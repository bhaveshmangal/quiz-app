from rest_framework.routers import DefaultRouter
from .views import StudentClassViewSet, QuizScoreViewSet

router = DefaultRouter()

router.register(r'student_class', StudentClassViewSet, basename='student_class')
router.register(r'score', QuizScoreViewSet, basename='quiz_score')

urlpatterns = router.urls