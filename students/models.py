from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission

class Student(AbstractUser):
    student_id = models.AutoField(primary_key=True)
    groups = models.ManyToManyField(Group, blank=True, related_name="student_groups")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="student_user_permissions")

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='books/covers/', blank=True, null=True) 
    
class BorrowedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    return_by = models.DateTimeField()

    class Meta:
        unique_together = ['student', 'book']

