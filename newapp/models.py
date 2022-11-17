from django.db import models

# Create your models here.

# Maxing out names of missing persons to 12 characters. First and Last both receive 12 each. 
class missing_person(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    date_missing = models.CharField(max_length=11)

    class Meta:
        db_table = "missing_persons"
