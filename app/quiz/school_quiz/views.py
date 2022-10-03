from rest_framework import viewsets
from rest_framework import mixins
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import StudentClass, User, ClassTest, StudentScore
from .serializers import StudentClassSerializer, UserSerializer, UserTokenObtainPairSerializer, ClassTestSerializer, StudentScoreSerializer


class StudentClassViewSet(viewsets.ModelViewSet):
    queryset = StudentClass.objects.all()
    serializer_class = StudentClassSerializer
    permission_classes = (IsAuthenticated,)


class UserObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = UserTokenObtainPairSerializer


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter_by_student_class(user.class_name)
        if self.action == "list":
            return queryset.filter(is_student=True)
        return queryset


class ClassTestViewSet(mixins.CreateModelMixin ,viewsets.GenericViewSet):
    queryset = ClassTest.objects.all()
    serializer_class = ClassTestSerializer
    permission_classes = (IsAuthenticated,)


class StudentScoreViewSet(viewsets.ModelViewSet):
    queryset = StudentScore.objects.all()
    serializer_class = StudentScoreSerializer
    permission_classes = (IsAuthenticated,)