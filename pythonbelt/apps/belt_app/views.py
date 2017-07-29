# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, HttpResponse
from .models import User

def index(request):
    return render(request, 'belt_app/index.html')

def login(request):
    if request.method == "POST":
        result = User.objects.login('request.POST')
        route = processLogin(request, result)
    return rediret(reverse(route))

def register(request):
    context= {

        "full_name" : request.POST['full_name'],
        "alias" : request.POST['alias'],
        "email" : request.POST['email'],
        "password" : request.POST['password'],
        "birthday" : request.POST['birthday']
    }
    if request.method == "POST":
        result = User.objects.registerUser('full_name', 'alias','email','password','birthday')
    return render('..pokey_app/index.html', context)

def processLogin(request, result):
    if result['status']:
        request.session['user_id'] = result['user_id']
    else:
        for error in result['errors']:
            messages.error(request, error['message'])
    return render(request, "belt_app/index.html")


def logout(request):
    request.session.clear()
    return redirect(reverse(root))
