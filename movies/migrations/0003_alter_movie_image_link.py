# Generated by Django 4.1.3 on 2022-11-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_image_link_movie_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
