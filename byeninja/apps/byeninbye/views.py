# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'byeninbye/index.html')

def ninjas(request):
    context = {
        "blue" : '',
        "red" : '',
        "yellow" : '',
        "purple" : ''
    }
    return render(request, 'byeinbye/ninjas.html', context)

def ninjashow(request, color):
    if color == blue:
        context = {
            "blue" : 'asdf'
        }
    elif color == red:
        context = {
            "red" : 'asdf'
        }
    elif color == yellow:
        context = {
            "yellow" : 'asdf'
        }
    elif color == purple:
        context = {
            "purple" : 'asdf'
        }
    return render(request, 'byeninbye/ninjas.html', context)