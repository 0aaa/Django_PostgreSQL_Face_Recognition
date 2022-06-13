from django.contrib.admin import ModelAdmin, TabularInline, site
from django.contrib import admin
from .models import Photo


class PhotoInline(TabularInline):
    model = Photo


site.register(Photo)


# class PhotoAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     inlines = [PhotoInline]


# admin.site.register(type(Photo), PhotoAdmin)