from django.contrib import admin
from .models import *

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('isim', 'user', 'slug')
    list_display_links = ('isim',)
    search_fields = ('isim',)
    list_filter = ('user',)
    # list_editable = ('user',)
    readonly_fields = ('slug', 'id')
# Register your models here.

admin.site.register(Profil, ProfilAdmin)
admin.site.register(Hesap)