import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('data.json', 'r', encoding='utf-8') as file:
            categories_list = []
            for category in json.load(file):
                if category['model'] == 'catalog.category':
                    categories_list.append(category)
        return categories_list

    @staticmethod
    def json_read_products():
        with open('data.json', 'r', encoding='utf-8') as file:
            product_list = []
            for product in json.load(file):
                if product['model'] == 'catalog.product':
                    product_list.append(product)
        return product_list

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(Category(name=category['fields']['name'],
                                                description=category['fields']['description']))
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(Product(name=product['fields']['name'],
                                              description=product['fields']['description'],
                                              image=product['fields']['image'],
                                              category=Category.objects.get(pk=product['fields']['category']),
                                              price=product['fields']['price'],
                                              created_at=product['fields']['created_at'],
                                              updated_at=product['fields']['updated_at']))
        Product.objects.bulk_create(product_for_create)
