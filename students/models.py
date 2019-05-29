from django.db import models

class Student(models.Model):
    pic = models.ImageField(default="images.png",blank= True)
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=10)
    classinfo = models.CharField(max_length=10)
    mothername = models.CharField(max_length=30)
    fathername = models.CharField(max_length=30)
    address = models.TextField()
    dob = models.DateField(blank=True)
    mobileno = models.IntegerField()
    email = models.EmailField()
    nationality = models.CharField(max_length=20)

    def __str__(self):
        return self.name
