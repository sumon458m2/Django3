from django.db import models

class client(models.Model):
    image=models.ImageField(upload_to='client/',blank=False)
    