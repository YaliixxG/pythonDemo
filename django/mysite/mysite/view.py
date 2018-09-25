
# -*- coding: utf-8 -*-


# from django.http import HttpResponse


# def hello(request):
#     return HttpResponse('<p>Hello,World!</p>')

from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World!!!!!'
    return render(request, 'hello.html', context)
