from django.db import models

class StudentInfo(models.Model):
    name = models.CharField(max=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone_no = models.CharField(max=15)

class TeacherInfo(models.Model):
    name = models.CharField(max=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone_no = models.CharField(max=15)
    experience = models.IntegerField()