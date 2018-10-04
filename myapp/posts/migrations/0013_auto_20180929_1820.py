# Generated by Django 2.1.1 on 2018-09-29 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20180928_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delete_Requested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_for_request', models.CharField(choices=[('Discriminatory', 'Discriminatory'), ('Offensive', 'Offensive'), ('Blackmail', 'Blackmail')], max_length=300)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Posts')),
            ],
        ),
        migrations.AlterField(
            model_name='recommend',
            name='post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='posts.Posts'),
        ),
    ]
