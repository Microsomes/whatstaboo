# Generated by Django 2.1.1 on 2018-09-28 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_posts_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='is_nsfw',
            field=models.BooleanField(default=False),
        ),
    ]
