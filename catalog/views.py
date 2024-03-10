from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        user_data = dict()
        user_data['name'] = request.POST.get('name')
        user_data['phone'] = request.POST.get('phone')
        user_data['message'] = request.POST.get('message')
        print(user_data)
        print(f"csrf_token: {request.POST['csrfmiddlewaretoken']}")
    return render(request, 'catalog/contacts.html')
