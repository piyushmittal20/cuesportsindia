# Generated by Django 3.1.4 on 2020-12-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newse',
            name='news_image',
            field=models.ImageField(blank=True, default='', upload_to='news/images'),
            preserve_default=False,
        ),
    ]
