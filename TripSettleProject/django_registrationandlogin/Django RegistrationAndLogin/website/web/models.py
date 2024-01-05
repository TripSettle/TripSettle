from django.db import models

# myapp/models.py

from django.db import models

class MyModel(models.Model):
    GroupName = models.CharField(max_length=255)
    TotalMembers = models.CharField(max_length=255)
    name=models.CharField(max_length=30)


# Create your models here.

class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)

    def __str__(self):
        return self.firstname + " " + self.lastname