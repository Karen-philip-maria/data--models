from django.db import models

class Course(models.Model):
    course_title= models.CharField(max_length=20)
    course_category= models.CharField(max_length=20)
    course_start_date= models.DateField()
    course_end_date = models.DateField()
    course_code =models.SmallIntegerField()
    teacher_code= models.SmallIntegerField()
    course_attendees= models.CharField(max_length=20)
# Create your models here.
