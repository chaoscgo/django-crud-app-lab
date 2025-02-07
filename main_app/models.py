from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    dupr = models.IntegerField()
    
    def __str__(self):
        return self.name