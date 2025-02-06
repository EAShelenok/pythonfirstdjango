from django.shortcuts import render
from django.views.generic import TemplateView

def platform(request):
    title = 'Main Page'
    head = 'Главная страница'
    url_main = 'Главная'
    url_games = 'Магазин'
    url_cart = 'Корзина'
    context = {
        'title': title,
        'header': head,
        'first_link': url_main,
        'second_link': url_games,
        'third_link': url_cart
    }
    return render(request, 'templ_platform.html', context)

def games(request):
    title = 'Game Catalogue'
    head = 'Игры'
    btn_buy = 'Купить'
    btn_back = 'Вернуться на главную'
    context={
        'title': title,
        'header': head,
        'b_buy': btn_buy,
        'b_back': btn_back
    }
    return render(request, 'templ_games.html', context)

def cart(request):
    title = 'Cart'
    head = 'Корзина'
    btn_back = 'Вернуться на главную'
    context={
        'title': title,
        'header': head,
        'b_back': btn_back
    }
    return render(request, 'templ_cart.html', context)