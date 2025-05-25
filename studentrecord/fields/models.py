from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=10)
    age = models.IntegerField(null=False)
    marks = models.FloatField()
    roll_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"
