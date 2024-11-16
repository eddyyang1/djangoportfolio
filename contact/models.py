from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.name
