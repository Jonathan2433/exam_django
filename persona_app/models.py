from django.db import models

# Create your models here.
class Persona(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    address_street = models.CharField(max_length=50)
    address_number = models.IntegerField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    picture = models.CharField(max_length=50)

    # def __str__(self):
    #     return str(self.id), self.first_name, self.last_name, 