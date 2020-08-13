from django.db import models
from phone_field import PhoneField

# Create your models here.

class Appointment(models.Model):
    name = models.CharField(max_length=256)
    phone = PhoneField(help_text = 'Contact phone no.')