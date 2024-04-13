from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(Base):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    # author = models.CharField(max_length = 30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} written by {self.author}'
    