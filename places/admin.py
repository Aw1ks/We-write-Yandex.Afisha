from django.contrib import admin
from .models import Place, Pictures_plase


class Pictures_plaseInline(admin.TabularInline):
    model = Pictures_plase
    extra = 1
    fields = ('image', 'order',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [Pictures_plaseInline,]


@admin.register(Pictures_plase)
class Pictures_plaseAdmin(admin.ModelAdmin):
    list_display = ('place', 'order')
    list_filter = ('place',)