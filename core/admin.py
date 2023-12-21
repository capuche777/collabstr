from django.contrib import admin
from .models import JsonFile


@admin.register(JsonFile)
class JsonFileAdmin(admin.ModelAdmin):
    list_display = ('uploaded_at',)
