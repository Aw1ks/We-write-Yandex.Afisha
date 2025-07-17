from django.db import models
from django.core.validators import MinValueValidator


class Place(models.Model):
    title = models.CharField('Название экскурсии', max_length=200)
    description_short = models.TextField('Краткое описание экскурсии', 
                                        default='Описание в разработке', 
                                        blank=True)
    description_long = models.TextField('Подробное описание экскурсии', 
                                        default='Описание в разработке', 
                                        blank=True)

    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')


    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.title


class Pictures_places(models.Model):
    place = models.ForeignKey(Place, 
                            on_delete=models.CASCADE, 
                            related_name='pictures')

    image = models.ImageField('Изображение места', 
                            upload_to='images', 
                            blank=True)

    order = models.PositiveIntegerField('Номер изображения', 
                            default=1,
                            validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ['order']

    def __str__(self):
        return f"{self.order} {self.place.title}"
