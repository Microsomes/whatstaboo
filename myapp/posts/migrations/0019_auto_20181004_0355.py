# Generated by Django 2.1.1 on 2018-10-04 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_auto_20181002_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='body',
            field=models.TextField(blank=True, default='---write something'),
        ),
    ]