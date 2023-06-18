from django.contrib import admin

from back.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'created_at', 'updated_at', 'published_at', 'author', 'status']
    list_filter = ['title',  'created_at', 'updated_at', 'published_at', 'author', 'status']


