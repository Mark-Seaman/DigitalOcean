# Generated by Django 4.0.5 on 2022-10-11 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_content_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='folder',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.content'),
        ),
    ]