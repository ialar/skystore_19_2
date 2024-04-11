from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'preview', 'created_at', 'is_published', 'views')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
