from django.db import models

#makemigrations - create changes and store in a  file.
#migrate - apply the pending changes created by makemigrations


# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.firstname
    
class Signup(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=8)
    date = models.DateField()
    
    def __str__(self):
        return self.username