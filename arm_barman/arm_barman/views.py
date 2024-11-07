from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    '''main'''

    return render(request, 'base.html')


def record_drinks(request):
    '''Учет продаж напитков'''

    return render(request, 'record_drinks.html')


def form_saves(request):
    '''Формирование отчетов о продажах напитков'''

    return render(request, 'form_saves.html')
