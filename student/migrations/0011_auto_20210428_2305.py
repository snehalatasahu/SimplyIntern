# Generated by Django 3.1.7 on 2021-04-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20210428_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='auth_token',
            field=models.CharField(default='', max_length=128),
        ),
    ]