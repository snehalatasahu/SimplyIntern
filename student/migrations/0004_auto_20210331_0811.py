# Generated by Django 3.1.7 on 2021-03-31 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_iscompany'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='cgpa',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='college',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='grad_year',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
