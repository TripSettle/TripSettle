from django.db import models

# Create your models here.

class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)

    def __str__(self):
        return self.firstname + " " + self.lastname
    

class MyModel(models.Model):
    date = models.CharField(max_length=30)
    group_name = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    expenditure = models.FloatField()

    def _str_(self):
        return f"{self.date} - {self.group_name} - {self.person}"