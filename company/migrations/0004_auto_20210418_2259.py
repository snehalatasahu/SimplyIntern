# Generated by Django 3.1.7 on 2021-04-18 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_internship_no_of_applicants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='no_of_applicants',
            field=models.IntegerField(default=0),
        ),
    ]
