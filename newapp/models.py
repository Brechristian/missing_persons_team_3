from django.db import models

# Create your models here.


class missing_person(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    date_missing = models.CharField(max_length=11)

    class Meta:
        db_table = "missing_persons"
