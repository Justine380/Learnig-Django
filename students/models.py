from django.db import models
#create your model here
class students(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255) 