from django.shortcuts import render

from catalog.models import Product


def home(request):
    context = {'object_list': Product.objects.all(),
               'title': 'Skystore каталог'}
    return render(request, 'catalog/home.html', context)


def product(request, pk):
    context = {'object': Product.objects.get(pk=pk)}
    return render(request, 'catalog/product.html', context)


def contacts(request):
    if request.method == 'POST':
        user_data = dict()
        user_data['name'] = request.POST.get('name')
        user_data['phone'] = request.POST.get('phone')
        user_data['message'] = request.POST.get('message')
        print(user_data)
        print(f"csrf_token: {request.POST['csrfmiddlewaretoken']}")

    context = {'title': 'Контакты'}

    return render(request, 'catalog/contacts.html', context)
