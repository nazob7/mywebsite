from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    print('Privet mir')
    return HttpResponse('Page with courses!')
# Create your views here.
