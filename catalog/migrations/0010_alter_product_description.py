# Generated by Django 4.2 on 2024-05-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_product_options_product_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, help_text='Введите описание продукта', null=True, verbose_name='Описание'),
        ),
    ]
