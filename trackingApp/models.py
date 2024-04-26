from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='LOW')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    photo = models.ImageField(upload_to='comment_photos/', null=True, blank=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.task.title}'

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class NoteComment(models.Model):
    note = models.ForeignKey(Note, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.note.title}'