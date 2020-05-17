
from django.db import models


# Create your models here.
from django.utils import timezone


# Testing..
class PostCategory(models.Model):
    Created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    Updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    CategoryName = models.CharField(max_length=255, verbose_name='CategoryName')

    class Meta:
        verbose_name = "PostCategory"
        verbose_name_plural = "PostCategories"
        ordering = ['CategoryName']

    def __str__(self):
        return self.CategoryName


class Post(models.Model):
    # Created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    Author_Name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Contents = models.TextField(max_length=1000)
    Created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created_at")
    Published_at = models.DateTimeField(
        blank=True, null=True, editable=False, verbose_name="Published at")
    is_published = models.BooleanField(default=False, verbose_name="Is published?")
    PostCategory = models.ForeignKey(
        PostCategory, verbose_name="PostCategory",
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-Created_at']

    def publish(self):
        self.is_published = True
        self.Published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.Title
