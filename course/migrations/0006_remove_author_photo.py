# Generated by Django 4.0.5 on 2022-08-30 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='photo',
        ),
    ]
