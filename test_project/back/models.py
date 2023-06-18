from django.db import models
from django.contrib.auth.models import User
from back.choices import PostStatusChoices


class Post(models.Model):
    title = models.CharField(max_length=32, default='', blank=True, verbose_name='post title')
    content = models.TextField(max_length=1024, default='', blank=True, verbose_name='post content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='post create date')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='post update date')
    published_at = models.DateTimeField(blank=True, null=True, verbose_name="post publish date")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts', verbose_name='post author')
    status = models.CharField(max_length=32, choices=PostStatusChoices, blank=True,
                              default=PostStatusChoices.unpublished, verbose_name='post status')
    image_b = models.ImageField(upload_to='post_images/', verbose_name='post big image')  # 600x1200
    image_s = models.ImageField(upload_to='post_images/', verbose_name='post small image')  # 300x800

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f'{self.title} {self.author}'
