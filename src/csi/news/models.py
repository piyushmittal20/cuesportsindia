from django.db import models
from datetime import datetime
NEWS_CATEGORY = (
    ('Latest','LATEST'),
    ('Featured', 'FEATURED'),
)
# Create your models here.
class Newse(models.Model):
    id = models.AutoField(primary_key=True)
    news_category = models.CharField(max_length=50, choices = NEWS_CATEGORY,default="")
    news_title = models.CharField(max_length=50,default="")
    news_desc = models.TextField(default="")
    news_image = models.ImageField(upload_to='news/images',blank=True)
    timestamp  = models.DateTimeField(null=True)

    def __str__(self):
        return self.news_title