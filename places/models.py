from django.db import models


class Place(models.Model):
    title = models.CharField('Название экскурсии', max_length=200)
    description_short = models.TextField('Краткое описание экскурсии', default='Описание в разработке', blank=True)
    description_long = models.TextField('Подробное описание экскурсии', default='Описание в разработке', blank=True)

    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title