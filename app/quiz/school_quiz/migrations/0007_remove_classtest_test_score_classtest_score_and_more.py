# Generated by Django 4.1.1 on 2022-10-02 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_quiz', '0006_classtest_testscore_delete_quizscore_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classtest',
            name='test_score',
        ),
        migrations.AddField(
            model_name='classtest',
            name='score',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='classtest',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='TestScore',
        ),
    ]
