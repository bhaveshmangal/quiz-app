# Generated by Django 4.1.1 on 2022-09-29 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_quiz', '0004_alter_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizscore',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
