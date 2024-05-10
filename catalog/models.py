from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание продукта', **NULLABLE)
    image = models.ImageField(upload_to='products_images/', verbose_name='Превью товаров', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', **NULLABLE)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    count_of_views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, verbose_name='Пользователь', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.name} ({self.category}) - {self.price} руб.'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)
        permissions = [('can_change_product_is_published_status', 'Can change publication status of product'),
                       ('can_change_product_description', 'Can change description of product'),
                       ('can_change_product_category', 'Can change category of product')]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', **NULLABLE)
    version_number = models.CharField(max_length=100, verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    is_active = models.BooleanField(default=False, verbose_name='Active')

    def __str__(self):
        return f'Версия {self.product} - {self.version_number}/{self.version_name} [{self.is_active}]'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('version_number',)
