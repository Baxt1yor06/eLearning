# Generated by Django 5.0.1 on 2024-03-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningapp', '0002_popular_courses_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructors',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
