from django.db import models

# Create your models here.


# Custom user model
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Example:
created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class User(AbstractUser):
    ROLE_CHOICES = [('student', 'Student'), ('instructor', 'Instructor')]
    role = models.CharField(choices=ROLE_CHOICES, max_length=10, default='student')
    verified = models.BooleanField(default=False)
    level_of_study = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username


# Course model
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    total_duration = models.DurationField()

# Module model
class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50, choices=[('pdf', 'PDF'), ('text', 'Text'), ('video', 'Video'), ('link', 'Link')])
    url_or_file = models.FileField(upload_to='modules/', blank=True, null=True)
    order = models.IntegerField()
    duration = models.DurationField()

# Progress model
class Progress(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='progress')
    progress_percent = models.FloatField()
    last_accessed_module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True, blank=True)

# Community model
class Community(models.Model):
    post_title = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

# Comment model
class Comment(models.Model):
    post = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# Organization model
class Organization(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

# Marketplace model
class Marketplace(models.Model):
    featured_courses = models.ManyToManyField(Course)

