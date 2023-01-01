# Generated by Django 4.0.4 on 2022-08-25 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_content'),
        ('student', '0002_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ForeignKey(default='1', editable=False, on_delete=django.db.models.deletion.CASCADE, to='course.course'),
        ),
    ]
