from django.db import models

# class Myproject(models.Model):

# Create your models here.

# class Samsung(models.Model):
#
#     id = models.AutoField(primary_key = True)
#     price = models.IntegerField(null=True)
#     date = models.DateField(unique=True)
#     positive = models.IntegerField(null=True)
#     negative = models.IntegerField(null=True)
#     neutral = models.IntegerField(null=True)

class Samsung(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    price = models.IntegerField(db_column='price', null=True)
    date = models.DateField(db_column='date', unique=True)
    positive = models.IntegerField(db_column='positive',null=True)
    negative = models.IntegerField(db_column='negative',null=True)
    neutral = models.IntegerField(db_column='neutral', null=True)

    class Meta:
        managed = True
        db_table = 'samsung'
