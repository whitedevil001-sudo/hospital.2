from django.db import models

# Create your models here.

class doctor(models.Model):
    Name= models.CharField( max_length=50)
    location=models.CharField( max_length=50)
    Type=models.CharField(max_length=50,choices=(('suregon','suregon'),('general','general')))
    Active=models.BooleanField(default=True)

    def __str__(self):
        return self.Name + "--"+self.location