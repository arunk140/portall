from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=2048)
    icon_class = models.CharField(max_length=2048)
    pub_date = models.DateTimeField('date published')
    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.category_name

class Shortcut(models.Model):
    url_path = models.CharField(max_length=2048)
    icon_class = models.CharField(max_length=2048)
    shortcut_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.shortcut_name