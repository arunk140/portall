from .models import Setting
import json

def app_settings(request):
    """Global values to pass to templates"""
    settings_dict = dict()
    settings = dict()
    for obj in Setting.objects.all():
        settings[obj.key] = obj.value
    settings_dict['settings'] = json.dumps(settings)
    return settings_dict