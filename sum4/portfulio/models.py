from django.db import models

# Create your models here.
class portfulio(models.Model):
    image=models.ImageField(upload_to='portfulio/',blank=False)
    link=models.CharField(max_length=1000,blank=False)
    name=models.CharField(max_length=100,blank=False)
    def __str__(self):
        return self.name
