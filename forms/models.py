from django.db import models

# Create your models here.

class Contact(models.Model):
    usn = models.IntegerField(default="")
    name = models.CharField(max_length=100, default="")
    semester = models.IntegerField(default="")
    mobile = models.IntegerField(default="")
    email = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name