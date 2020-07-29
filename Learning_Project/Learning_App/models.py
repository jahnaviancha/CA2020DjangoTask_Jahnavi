from django.db import models


# Create your models here.


class classes(models.Model):
    Name=models.CharField(max_length=45)
    ID=models.AutoField(primary_key=True)
    Contact=models.IntegerField(null=False, blank=False, unique=True)
    Address=models.CharField(max_length=500)