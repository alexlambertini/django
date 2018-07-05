from django.shortcuts import render
from .models import Person
from django.http import HttpResponse

# Create your views here.


def lista_clientes(request):
    persons = Person.objects.all()
    return render(request, 'listagem.html', {'persons': persons})


def teste(request):
    return HttpResponse('porra caraio')
