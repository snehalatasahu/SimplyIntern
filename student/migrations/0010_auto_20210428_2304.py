# Generated by Django 3.1.7 on 2021-04-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20210428_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='auth_token',
            field=models.UUIDField(default=''),
        ),
    ]
