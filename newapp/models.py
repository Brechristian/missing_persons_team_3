from django.db import models

# Create your models here.

# Maxing out names of missing persons to 12 characters. First and Last both receive 12 each.


class missing_person(models.Model):
    date_missing = models.CharField(max_length=11)
    last_name = models.CharField(max_length=12)
    first_name = models.CharField(max_length=12)
    age_at_missing = models.CharField(max_length=2, null=True, blank=True)
    city = models.CharField(max_length=12, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    race = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return self.first_name, self.last_name

    class Meta:
        db_table = "missing_persons"
