# Generated by Django 3.1.4 on 2020-12-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tournament_name', models.CharField(default='', max_length=50)),
                ('sport_category', models.CharField(choices=[('Billiards', 'BILLIARDS'), ('Snooker', 'SNOOKER'), ('Pool', 'POOL')], default='', max_length=50)),
                ('Destination_category', models.CharField(choices=[('National', 'NATIONAL'), ('INTERNATIONAL', 'INTERNATIONAL')], default='', max_length=50)),
                ('entry_fee', models.IntegerField(default=0)),
                ('prize_money', models.IntegerField(default=0)),
                ('tournament_image1', models.ImageField(upload_to='mycsi/images')),
                ('tournament_venue', models.TextField()),
                ('tournament_startdate', models.DateTimeField(null=True)),
                ('tournament_enddate', models.DateTimeField(null=True)),
                ('tournament_desc', models.TextField()),
                ('bank_name', models.CharField(default='', max_length=500)),
                ('bank_address', models.TextField(default='')),
                ('last_date_of_entry', models.DateTimeField(null=True)),
                ('account_number', models.PositiveBigIntegerField(default=0)),
                ('ifsc_code', models.PositiveBigIntegerField(default=0)),
                ('paytm_number', models.PositiveBigIntegerField(default=0)),
                ('name1', models.CharField(default='', max_length=100)),
                ('name2', models.CharField(default='', max_length=100)),
                ('contact_num1', models.PositiveBigIntegerField(default=0)),
                ('contact_num2', models.PositiveBigIntegerField(default=0)),
            ],
        ),
    ]
