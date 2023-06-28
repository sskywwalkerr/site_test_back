from django.shortcuts import render


def index(reguest):
    data = {
        'title': 'Главная страница',
    }
    return  render(reguest, 'main/index.html',data)

def about(reguest):
    return  render(reguest, 'main/about.html')