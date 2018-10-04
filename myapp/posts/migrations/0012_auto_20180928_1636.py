# Generated by Django 2.1.1 on 2018-09-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20180928_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_settings',
            name='site_status_is_production',
            field=models.CharField(choices=[('FR', 'Active'), ('SO', 'Inactive'), ('JR', 'In Selling'), ('SR', 'No longer supported')], max_length=300),
        ),
    ]
