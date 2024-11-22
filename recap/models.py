from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='student_images',blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"