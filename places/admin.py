from django.contrib import admin
from django.utils.html import mark_safe

from .models import Place, Pictures_places


WIDTH = 300
HEIGHT = 200


class Pictures_placeInline(admin.TabularInline):
    model = Pictures_places
    extra = 1
    fields = ('image', 'get_preview', 'order',)
    readonly_fields = ('get_preview',)

    def get_preview(self, obj):
        image = obj.image
        if image:
            return mark_safe(f'<img src="{image.url}" style="max-width: {WIDTH}px; max-height: {HEIGHT}px;" />')
        return None

    get_preview.short_description = 'GET PREVIEW'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', )

    inlines = [Pictures_placeInline, ]


@admin.register(Pictures_places)
class Pictures_placeAdmin(admin.ModelAdmin):
    list_display = ('place', 'order')
    list_filter = ('place',)