from django.db import models
from django.core.validators import MinValueValidator
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название экскурсии', max_length=200)
    short_description = models.TextField('Краткое описание экскурсии', 
                                        default='Описание в разработке', 
                                        blank=True)
    long_description = HTMLField('Подробное описание экскурсии', 
                                        default='Описание в разработке', 
                                        blank=True)

    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, 
                            on_delete=models.CASCADE, 
                            related_name='pictures')

    image = models.ImageField('Изображение места', upload_to='images')

    order = models.PositiveIntegerField('Номер изображения',
                                        default=1,
                                        validators=[MinValueValidator(1)],
                                        db_index=True)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ['order']

    def __str__(self):
        return f"{self.order} {self.place.title}"
