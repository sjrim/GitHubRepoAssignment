# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..belt_app.models import User

class PokeyManager(models.Manager):
    def Pokey(self, id, useid):
        try:
            userToPoke = User.objects.get(id=id)
            loggedUser = User.objects.get(id=useid)
            Pokey.objects.create(poker=loggedUser, poki=userToPoke)
        except:
            print "no User with id {}".format(id)

class Pokey(models.Model):
    poker = models.ForeignKey(User, related_name="pokes_made")
    poki = models.ForeignKey(User, related_name="pokes_received")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = PokeyManager()

# Create your models here.
