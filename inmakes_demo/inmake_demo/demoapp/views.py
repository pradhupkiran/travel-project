from django.contrib.auth import models
from django.shortcuts import render
from .models import Place, Team


# Create your views here.
def index(request):
    ob1 = Place.objects.all()
    team = Team.objects.all()
    return render(request, 'index.html', {'ob1': ob1,'team':team})


def about(request):
    abouts = {
        'mail': 'comapany@mail.com',
        'ph': 58456456,

    }
    return render(request, 'about.html', abouts)


def contact(request):
    return render(request, 'contact.html')


def detail(request):
    return render(request, 'detail.html')


def thanks(request):
    return render(request, 'thanks.html')


def opreartion(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    return render(request, 'result.html', {'add': add, 'sub': sub, 'mul': mul, 'div': div})
