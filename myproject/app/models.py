# models.py

from django.db import models
from django.core.exceptions import ValidationError


class Task(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    status_choices = (
        ('completed', 'Completed'),
        ('pending', 'Pending'),
    )
    status = models.CharField(max_length=20, choices=status_choices, default='pending')

    # below for validattion clean method is a place to put any additional validation logic that goes beyond what can -
    # be expressed using Django model field options (e.g., max_length, choices, etc.).

    def clean(self):             

         # Check if the 'title' field is empty
        if not self.title:
            raise ValidationError("Title cannot be empty")
        
        # Check if the 'body' field is empty
        if not self.body:
            raise ValidationError("Body cannot be empty")
        
        # Check if the 'status' field is left unchecked
        if not self.status:
            raise ValidationError("Status cannot be empty")
    

    def __str__(self):
        return self.title
