from django.contrib import admin
from .models import Setting

# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'key', 'value']
    readonly_fields = ['name', 'key']
     # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False
    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Setting, SettingAdmin)