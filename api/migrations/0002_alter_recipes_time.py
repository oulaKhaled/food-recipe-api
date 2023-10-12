# Generated by Django 4.2.5 on 2023-10-04 11:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='time',
            field=models.IntegerField(choices=[], null=True, validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(0)]),
        ),
    ]