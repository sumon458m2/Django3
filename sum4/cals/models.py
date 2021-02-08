from django.db import models
class about(models.Model):
    title=models.CharField(max_length=100,blank=False)
    description=models.TextField(max_length=1000,blank=False)
    image=models.ImageField(upload_to='about/',blank=False)
    def __str__(self):
        return self.title


class test(models.Model):
    name=models.CharField(max_length=100,blank=False)
    description=models.TextField(max_length=1000,blank=False)
    
    def __str__(self):
        return self.name

class Team(models.Model):
    name=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='team/',blank=False)
    def __str__(self):
        return self.name


class testmonial(models.Model):
    title=models.CharField(max_length=100,blank=False)
    description=models.TextField(max_length=1000,blank=False)
    image=models.ImageField(upload_to='testmonial/',blank=False)
    def __str__(self):
        return self.title