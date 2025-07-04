from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    categories = models.ManyToManyField('Category', related_name='posts')
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class PostViewCount(models.Model):
    posts = models.OneToOneField('Post', on_delete=models.CASCADE, related_name='view_count')
    visitor = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('posts', 'visitor')

    def __str__(self):
        return f'{self.posts.title} - {self.visitor.username}'
