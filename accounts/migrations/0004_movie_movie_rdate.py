# Generated by Django 2.2.3 on 2019-09-01 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_movie_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_rdate',
            field=models.CharField(default='null', max_length=20),
        ),
    ]
