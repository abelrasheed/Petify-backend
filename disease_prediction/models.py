from django.db import models


# Create your models here.
class Disease(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True, blank=False)
    description = models.TextField(max_length=200,blank=True)
    symptoms = models.TextField(max_length=100,blank=True)

    def __str__(self):
        return self.name