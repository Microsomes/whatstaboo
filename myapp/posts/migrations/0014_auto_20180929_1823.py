# Generated by Django 2.1.1 on 2018-09-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20180929_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='delete_requested',
            name='your_email',
            field=models.EmailField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='delete_requested',
            name='your_name',
            field=models.CharField(default='', max_length=300),
        ),
    ]