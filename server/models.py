from django.db import models


class user_registration(models.Model):
    Id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=40)
    Email = models.CharField(max_length=50)
    Age=models.IntegerField()
    Date_of_Birth=models.DateField()
