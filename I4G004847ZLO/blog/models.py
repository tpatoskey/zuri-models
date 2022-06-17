from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

Author = get_user_model()

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=100)
    Text = models.TextField()
    Author = models.ForeignKey(Author, on_delete= models.CASCADE)
    Created_date = models.DateTimeField(default=datetime.now)
    Published_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.Author.Author

