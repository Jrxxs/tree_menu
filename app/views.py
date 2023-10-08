from django.shortcuts import render
from .models import Category


def index(request):
    Menus = Category.objects.filter(parent=None)
    return render(request, 'index.html', context={'Menus': Menus})

def menu(request, id):
    Data = Category.objects.get(id=id)
    return render(request, 'menu.html', context={'Data': Data.name})