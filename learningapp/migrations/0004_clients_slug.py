# Generated by Django 5.0.1 on 2024-03-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningapp', '0003_instructors_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]