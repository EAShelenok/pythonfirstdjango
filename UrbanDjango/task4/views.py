from django.shortcuts import render

def platform(request):
    title = 'Main Page'
    head = 'Главная страница'
    context = {
        'title': title,
        'head': head
    }
    return render(request, 'templ_platform.html', context)

def games(request):
    title = 'Game Catalogue'
    head = 'Игры'
    btn_buy = 'Купить'
    btn_back = 'Вернуться на главную'
    context = {
        'title': title,
        'head': head,
        'b_buy': btn_buy,
        'b_back': btn_back,
        'games': ['Atomic Heart','Cyberpunk 2077', 'PayDay 2', 'Silent Hill 2', 'Alan Wake 2']
    }
    return render(request, 'templ_games.html', context)

def cart(request):
    title = 'Cart'
    head = 'Корзина'
    btn_back = 'Вернуться на главную'
    context = {
        'title': title,
        'head': head,
        'b_back': btn_back
    }
    return render(request, 'templ_cart.html', context)