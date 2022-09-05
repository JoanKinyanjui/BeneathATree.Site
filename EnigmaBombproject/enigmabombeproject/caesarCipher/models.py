from django.db import models

class Messages(models.Model):
    writtenmessage=models.CharField(max_length=255)
    cipheredmessage=models.CharField(max_length=255)
    decipheredmessage=models.CharField(max_length=255)
   
