# Generated by Django 4.0.4 on 2022-10-02 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_remove_demo_course_remove_lesson_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='week',
            field=models.IntegerField(default=7),
        ),
    ]
