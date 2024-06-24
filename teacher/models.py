from django.db import models

class Teachers(models.Model):
    first_name =  models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    student_code =models.SmallIntegerField()
    email=models.EmailField()
    age= models.SmallIntegerField()
    country= models.CharField(max_length=20)
    phone_number = models.DateField()
    date_of_birth= models.DateField()
    immediate_contact = models.CharField(max_length=20)
    image = models.ImageField()
    bio = models.TextField()
# Create your models here.
