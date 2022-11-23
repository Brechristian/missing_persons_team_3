from django.db import models

# Create your models here.

# Maxing out names of missing persons to 12 characters. First and Last both receive 12 each.


class missing_person(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    date_missing = models.CharField(max_length=11)
    age_at_missing = models.CharField(max_length=2)
    city = models.CharField(max_length=12)
    state = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=1)

    def __str__(self):
        return self.first_name, self.last_name

    class Meta:
        db_table = "missing_persons"
