from django.contrib.admin import ModelAdmin, TabularInline, site
from .models import Photo


class PhotoInline(TabularInline):
    model = Photo


class PhotoAdmin(ModelAdmin):
    list_display = ('name', 'status',)


site.register(Photo, PhotoAdmin)