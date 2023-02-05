from django.db import models
# from django.db import forms

# Create your models here.
ROLE_CHOICES = (('R', "Regular - Can't delete members"), ('A', "Admin - Can delete members"))
class Members(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)

    def __str__(self):
        return self.first_name

    

