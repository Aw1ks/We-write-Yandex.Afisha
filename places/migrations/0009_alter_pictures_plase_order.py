# Generated by Django 5.2.3 on 2025-06-26 15:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_pictures_plase_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures_plase',
            name='order',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Номер изображения'),
        ),
    ]
