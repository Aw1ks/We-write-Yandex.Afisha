from django.contrib import admin
from django.utils.html import mark_safe
from adminsortable2.admin import SortableTabularInline, SortableAdminBase

from .models import Place, Pictures_places


MAX_WIDTH = 300
MAX_HEIGHT = 200


class Pictures_placeInline(SortableTabularInline, admin.TabularInline):
    model = Pictures_places
    extra = 1
    fields = ('image', 'get_preview', 'order',)
    readonly_fields = ('get_preview',)

    def get_preview(self, obj):
        image = obj.image
        if image:
            return mark_safe(f'<img src="{image.url}" style="max-width: {MAX_WIDTH}px; max-height: {MAX_HEIGHT}px;" />')
        return None

    get_preview.short_description = 'PREVIEW'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', )

    inlines = [Pictures_placeInline, ]


@admin.register(Pictures_places)
class Pictures_placeAdmin(admin.ModelAdmin):
    fields = ("image", "get_preview", "place", "order",)
    raw_id_fields = ["place", ]