# Generated by Django 2.2 on 2020-08-09 03:57

import Learning_App.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learning_App', '0004_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=40, validators=[Learning_App.models.name]),
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=50, validators=[Learning_App.models.check]),
        ),
    ]
