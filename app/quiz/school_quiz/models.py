from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class StudentClass(models.Model):
    number = models.IntegerField(null=True, blank=True)
    section = models.CharField(max_length=2)
    students = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.number) + self.section


class QuizUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""

        class_name = StudentClass.objects.create(number=00)
        extra_fields.update({'class_name':class_name})
    
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username=None

    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    class_name = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = QuizUserManager()

    def __str__(self):
        return self.email

    
class StudentQuerySet(models.QuerySet):
    def filter_by_student_class(self, class_name):
        return self.filter(class_no=class_name)


class ClassTest(models.Model):
    test_date = models.DateField()
    class_name = models.ForeignKey(StudentClass, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.test_date)


class StudentScore(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(null=True)
    test = models.ForeignKey(ClassTest, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.student   