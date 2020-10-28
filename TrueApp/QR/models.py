from django.db import models

# Create your models here.



class TrueApp(models.Model):

    app_name = models.CharField(max_length = 100)
    android_url = models.CharField(max_length = 300)
    iphone_url = models.CharField(max_length = 300)

    def __str__(self):
        return self.app_name