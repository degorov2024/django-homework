from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now()
    msg = f'Текущее время на сервере: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    files_list = '<br/>'.join(os.listdir(path='.'))
    msg = f'<p>Содержимое рабочей директории:</p>{files_list}'
    return HttpResponse(msg)
