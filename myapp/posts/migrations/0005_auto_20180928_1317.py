# Generated by Django 2.1.1 on 2018-09-28 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_featuredbyeditors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeaturedByEditors',
            new_name='EditorsChoice',
        ),
        migrations.AlterModelOptions(
            name='editorschoice',
            options={'verbose_name_plural': 'Editors Choice'},
        ),
    ]