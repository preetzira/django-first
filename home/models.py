from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    username = models.CharField(max_length=35)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zip = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.fname+" "+self.lname
    