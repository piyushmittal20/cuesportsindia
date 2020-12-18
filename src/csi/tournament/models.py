from django.db import models
from datetime import datetime
SPORT_CHOICES = (
    ('Billiards','BILLIARDS'),
    ('Snooker', 'SNOOKER'),
    ('6Reds', '6REDS'),
    ('10Reds','10REDS'),
    ('Pool','POOL'),
    ('Carrom','CARROM'),
)
EVENT_CHOICES = (
    ('IBSF','IBSF'),
    ('ACBS','ACBS'),
    ('National','NATIONAL'),
    ('Invitation','INVITATION'),
    ('Open Entry','OPEN ENTRY'),
    ('Professional','PROFESSIONAL'),
)

class Tournament(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_name = models.CharField(max_length=50, default="")
    event_category = models.CharField(max_length=50, choices = EVENT_CHOICES,default="")
    sports_category = models.CharField(max_length=50, choices = SPORT_CHOICES,default="")
    entry_fee = models.IntegerField(default=0)
    prize_money = models.IntegerField(default=0)
    tournament_image1 = models.ImageField(upload_to='tournament/images')
    tournament_image2 = models.ImageField(upload_to='tournament/images',blank=True)
    tournament_venue = models.TextField()
    tournament_startdate = models.DateTimeField(null=True)
    tournament_enddate = models.DateTimeField(null=True)
    tournament_desc = models.TextField()
    # bank details
    bank_name = models.CharField(max_length=500, default="")
    last_date_of_entry = models.DateTimeField(null=True)
    account_number = models.PositiveBigIntegerField(default=0)
    ifsc_code = models.CharField(max_length=100, blank=True)
    paytm_number = models.CharField(max_length=15,default="")
    # contact details
    # name1 = models.CharField(max_length=100,default="",)
    # name2 = models.CharField(max_length=100, default="",blank=True)
    # name3 = models.CharField(max_length=100, default="",blank=True)
    # name4 = models.CharField(max_length=100, default="",blank=True)
    # contact_num1 = models.charField(max_length=15,default="")
    # contact_num2 = models.charField(max_length=15,default="",blank=True)
    # contact_num3 = models.charField(max_length=15,default="",blank=True)
    # contact_num4 = models.charField(max_length=15,default="",blank=True)

    def __str__(self):
        return self.tournament_name