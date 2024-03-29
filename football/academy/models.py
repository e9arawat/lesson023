"""
    Module name :- models
    Classes :- StudentInfo, TeacherInfo
"""

from django.db import models


class StudentInfo(models.Model):
    """
    Data model for student.
    """

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name}"


class TeacherInfo(models.Model):
    """
    Data model for teacher.
    """

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    experience = models.IntegerField()

    def __str__(self):
        return f"{self.name}"
