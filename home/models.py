from django.db import models

#make migrations - create changes and store in file
#migrate -apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone =models.CharField(max_length=12)
    email =models.CharField(max_length=100)
    desc =models.TextField()
    date =models.DateField()


    def __str__(self):
        return self.name