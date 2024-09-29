from django.db import models

# Create your models here.
class Registration(models.Model):
    NAME = models.CharField(max_length=50)
    USER_NAME = models.CharField(max_length=150)
    CATAGORY = models.CharField(max_length=50)
    EMAIL = models.EmailField(max_length=254)
    PHONE = models.CharField(max_length=50)
    PASSWORD = models.CharField(max_length=250)
    CREATED_AT= models.DateTimeField(auto_now_add=True)
 

class Docters(models.Model):
    NAME = models.CharField(max_length=50)
    USER_NAME = models.CharField(max_length=50)
    CATAGORY = models.CharField(max_length=50)
    EMAIL = models.EmailField(max_length=254)
    PHONE = models.CharField(max_length=50)   
    
class Staffs(models.Model):
    NAME = models.CharField(max_length=50)
    USER_NAME = models.CharField(max_length=50)
    CATAGORY = models.CharField(max_length=50)
    EMAIL = models.EmailField(max_length=254)
    PHONE = models.CharField(max_length=50)   
    
class Patients(models.Model):
    NAME = models.CharField(max_length=50)
    USER_NAME = models.CharField(max_length=50)
    CATAGORY = models.CharField(max_length=50)
    EMAIL = models.EmailField(max_length=254)
    PHONE = models.CharField(max_length=50)
    
class Bookings(models.Model):
    NAME = models.CharField(max_length=50)
    AGE  = models.IntegerField(null=True,blank=True)
    PHONE = models.CharField(max_length=50)
    EMAIL = models.EmailField(null=True,blank=True)
    TOKEN = models.IntegerField(default=100,null=True,blank=True)