from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

menu= ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts':posts, 'menu':menu, 'title':'Главная страница'})

def about(request):
    return render(request, 'women/about.html', {'menu':menu, 'title':'О сайте'})

def categories(request, catid):
    return HttpResponse(f"<h1>Статья по категориям</h1><p>{catid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')