# Generated by Django 5.2.3 on 2025-07-17 17:58

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_alter_pictures_places_options_alter_place_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, default='Описание в разработке', verbose_name='Подробное описание экскурсии'),
        ),
    ]
