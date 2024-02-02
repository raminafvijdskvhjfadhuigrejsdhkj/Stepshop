from django.shortcuts import render

def get_menu(view):

    links_menu = [
        {"href": "main:index", "name": "Главная ", "active": False},
        {"href": "main:products", "name": "Продукты", "active": False},
        {"href": "main:about", "name": "о  нас", "active": False},
        {"href": "main:contacts", "name": "Контакты", "active": False}

    ]
    for item in links_menu:
        if item["href"].split(':')[1] == view:
            item["active"] = True
    return links_menu

def index(request):
    title = 'Главная страница'
    context = {
        'title': title,
        'links_menu': get_menu(index)
    }
    return render(request, 'index.html', context)

def products(request):
    title = 'Главная Продукты'
    context = {
        'title': title,
        'links_menu': get_menu(products)
    }
    return render(request, 'products.html')

def product(request):

    context = {
        'title': title,
        'links_menu': get_menu(products)
    }
    return render(request, 'product.html')

def about(request):
    title = 'о  нас'
    context = {
        'title': title,
        'links_menu': get_menu(about)
    }
    return render(request, 'about.html')

def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
        'links_menu': get_menu(contacts)
    }
    return render(request, 'contacts.html')
