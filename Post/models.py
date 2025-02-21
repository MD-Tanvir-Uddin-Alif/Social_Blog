from django.db import models
# from Profile import models as profile_model
from django.contrib.auth.models import User
# Create your models here.

class Post_Model(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_like', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title}"


class Comment_Model(models.Model):
    post = models.ForeignKey('Post_Model', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comment by {self.author} on {self.post}'