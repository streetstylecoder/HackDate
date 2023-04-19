from django.db import models

# Create your models here.
class Hackathon(models.Model):
    name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    prize_money = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date=models.DateField()
    Apply = models.URLField()
    def __str__(self):
        return self.name

class Fest(models.Model):
    name=models.CharField(max_length=255)
    venue=models.CharField(max_length=255)
    description=models.TextField()
    checkout=models.URLField()
    def __str__(self):
        return self.name
    
class Esummit(models.Model):
    name=models.CharField(max_length=255)
    venue=models.CharField(max_length=255)
    description=models.TextField()
    checkout=models.URLField()
    def __str__(self):
        return self.name
    
