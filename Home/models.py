from django.db import models
from django.utils import timezone
timezone.now()

# Created  models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    phone= models.CharField(max_length=12)
    email= models.CharField(max_length=122)
    desc= models.TextField()
    date = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.name
        
