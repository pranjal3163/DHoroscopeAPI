from django.db import models
from django.utils import timezone
from datetime import date

class HoroscopeItem(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    sign_name= models.TextField(blank=True)
    date_range = models.TextField(blank=True)
    current_date = models.DateField(default=date.today)
    description= models.TextField(blank=True)
    compatibility=models.TextField(blank=True)
    mood=models.TextField(blank=True)
    color=models.TextField(blank=True)
    lucky_number=models.TextField(blank=True)
    lucky_time=models.TextField(blank=True)
