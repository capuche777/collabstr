from django.contrib import admin
from .models import Creator, Content


@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ('user', 'platform', 'rating')
    list_filter = ('platform', )
    search_fields = ('platform', 'user__username')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('user', 'url')
