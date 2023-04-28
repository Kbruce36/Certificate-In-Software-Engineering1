from django.db import models

# Create your models here.

class Registration(models.Model):
    firstname = models.CharField(max_length=100,null=True,blank=False)
    lastname = models.CharField(max_length=100,null=True,blank=False)
    date_of_birth = models.DateField(max_length=100,null=True,blank=False)
    gender = models.CharField(max_length=100,null=True,blank=False)
    country = models.CharField(max_length=100,null=True,blank=False)
    state_district = models.CharField(max_length=100,null=True,blank=False)
    town = models.CharField(max_length=100,null=True,blank=False)
    zipcode = models.CharField(max_length=100,null=True,blank=False)
    phone1 = models.CharField(max_length=100, null=True,blank=False)
    phone2 = models.CharField(max_length=100, null=True,blank=False)
    email = models.EmailField(max_length=1000,null=True,blank=False)
    def __str__(self):
        return self.firstname