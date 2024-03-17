# Generated by Django 5.0.3 on 2024-03-13 06:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=300)),
                ('rating', models.FloatField(default=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('type', models.CharField(choices=[('Beach', 'Beach'), ('Hill', 'Hill'), ('Fountain', 'Fountain'), ('Landmark', 'Landmark')], max_length=20)),
            ],
        ),
    ]