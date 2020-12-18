from django.db import models

# Create your models here.

class Sponser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    Banner = models.ImageField(upload_to="home/images")
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name
