from django.db import models

# Create your models here.



class TrueApp(models.Model):

    app_name = models.CharField(max_length = 100)
    android_url = models.URLField()
    iphone_url = models.URLField()
    web_url = models.URLField(default='test.com')


    def __str__(self):
        return self.app_name