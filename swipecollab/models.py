from django.db import models

# Create your models here.

class swipeprofile(models.Model):
    name=models.CharField(max_length=100)
    Looking_for=models.CharField(max_length=100)
    Description=models.TextField()
    analyse_profile=models.CharField(max_length=100)


class savematches(models.Model):
    name=models.CharField(max_length=100,default="match name")
    userid_sender=models.BinaryField()
    userid_rec=models.BinaryField()
