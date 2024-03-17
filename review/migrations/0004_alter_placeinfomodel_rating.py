# Generated by Django 5.0.3 on 2024-03-14 05:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_placeinfomodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeinfomodel',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]