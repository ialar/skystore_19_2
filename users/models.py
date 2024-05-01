from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='user_pictures/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=25, verbose_name='Номер телефона', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    verification_code = models.CharField(max_length=20, verbose_name='Код верификации', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
