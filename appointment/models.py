from django.db import models

# Create your models here.

class parchi(models.Model):
    Sr_No=models.PositiveIntegerField()
    Name=models.CharField(max_length=50)
    Start_time=models.TimeField()
    End_time=models.TimeField()
    def __str__(self):
        return self.Name
