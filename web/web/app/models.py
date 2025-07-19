from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField()
    content = models.TextField()
