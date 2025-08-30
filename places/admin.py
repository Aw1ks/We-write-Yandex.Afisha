from django.contrib import admin
from django.utils.html import mark_safe
from adminsortable2.admin import SortableTabularInline, SortableAdminBase

from .models import Place, Image


MAX_WIDTH = 300
MAX_HEIGHT = 200


class ImageInline(SortableTabularInline, admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image', 'get_preview', 'order',)
    readonly_fields = ('get_preview',)

    def get_preview(self, obj):
        image = obj.image
        if image:
            return format_html(
                '<img src="{}" style="max-width: {}px; max-height: {}px;" />',
                image.url,
                MAX_WIDTH,
                MAX_HEIGHT,
            )
        return None

    get_preview.short_description = 'PREVIEW'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', )

    inlines = [ImageInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ("image", "get_preview", "place", "order",)
    raw_id_fields = ["place", ]