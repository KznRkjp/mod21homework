from django.contrib import admin
from url_count.models import Url

@admin.register(Url)
class UrlCountAdmin(admin.ModelAdmin):
    list_display = ('job','url_link', 'status', 'date')
