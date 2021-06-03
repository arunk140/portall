from django.db import models

# Create your models here.
class Setting(models.Model):
    """
    Model for site-wide settings.
    """
    name = models.CharField(max_length=200, help_text="Name of site-wide variable")
    key = models.CharField(max_length=200, help_text="Key of site-wide variable")
    value = models.CharField(max_length=2000, null=True, blank=True, help_text="Value of site-wide variable that scripts can reference")
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name