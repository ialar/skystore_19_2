from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        user = dict()
        user['name'] = request.POST.get('name')
        user['phone'] = request.POST.get('phone')
        user['message'] = request.POST.get('message')
        print(user)
    return render(request, 'catalog/contacts.html')
