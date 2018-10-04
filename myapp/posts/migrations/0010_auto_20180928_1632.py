# Generated by Django 2.1.1 on 2018-09-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_app_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='app_settings',
            name='site_owned_by_company_or_name',
            field=models.CharField(default='Phase5 productions', max_length=400),
        ),
        migrations.AddField(
            model_name='app_settings',
            name='site_status_is_production',
            field=models.CharField(default=False, max_length=300),
        ),
    ]
