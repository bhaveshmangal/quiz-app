from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import StudentClass, User, ClassTest

class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = ('number', 'section', 'students')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = ('number', 'section')


class UserSerializer(serializers.ModelSerializer):
    class_name = StudentSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'class_name')


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = UserSerializer(self.user).data
        return data


class ClassTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassTest
        fields = ('test_date', 'class_name')