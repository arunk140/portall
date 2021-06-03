from django.contrib import admin

# Register your models here.
from .models import Category, Shortcut

class ShortcutAdmin(admin.ModelAdmin):
    list_display = ['shortcut_name', 'category', 'pub_date']

admin.site.register(Category)
admin.site.register(Shortcut, ShortcutAdmin)