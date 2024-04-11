from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=200, verbose_name='Слаг статьи', **NULLABLE)
    content = models.TextField(verbose_name='Cодержимое')
    preview = models.ImageField(upload_to='blogpost_images/', verbose_name='Превью статьи', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'"{self.title}" (дата создания: {self.created_at})'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('created_at',)
