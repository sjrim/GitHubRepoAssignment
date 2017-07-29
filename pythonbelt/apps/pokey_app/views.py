# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from ..belt_app.models import User
from .models import Pokey
from django.db.models import Count

root = 'pokey_app.home'
login_root = 'belt_app:root'

def home(request):
    if 'user_id' in request.ession:
        useid = request.session['user_id']
        loggedUser = User.objects.get(id=useid)
        poked_by = loggedUser.pokes_received.all().values("poker_name").annotatedCount('id').order_by('-id_count')
        otherUsers = User.objects.exclude(id=useid)
        context = {
            'loggeduser':loggedUser,
            'otherUsers':otherUsers,
            'poked_by':poked_by,
        }
def pokey(request, id):
    if 'user_id' in request.session:
        useid = request.session['user_id']
        Pokey.objects.pokey(id, useid)
        return redirect(reverse(root))
    return redirect(reverse(belt_app))

# Create your views here.
