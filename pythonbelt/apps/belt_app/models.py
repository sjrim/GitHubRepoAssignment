# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]*$')

class UserManager(models.Manager):
    def registerUser(self, full_name, alias, email, password, password_confirmation, birthday):
        errors = {}
        if len(full_name) < 1:
            errors['full_name'] = "Name needs to be enetered"

        if len(alias) < 1:
            errors['alias'] = "Alias needs to be entered"

        if len(password) < 8:
            errors['password'] = "Password needs to be at least eight characters long"

        if password != password_confirmation:
            errors['password'] = "Passwords do not match"
        try:
            existingUser = self.get(email__iexact=email)
        except:
            existingUser = None
        if existingUser:
            errors['email'] = 'That email is already registered'

        if not EMAIL_REGEX.match(email):
            errors['email'] = 'Invalid email.'

        if birthday == None:
            error['birthday'] = 'Please enter a birthday'

        if errors:
            return (False, errors)
        else:
            password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            self.create(email=email, name=name, alias=alias, password=password, birthday=birthday)

            return (True, self.get(email=email))

    def login(self, email, password):
        try:
            user = self.get(email__iexact=email)
        except:
            user = None
        if user and bcrypt.hashpw(password.encode('utf-8'), user.password.encode('utf-8')) == user.password.encode('utf-8'):
            return (True, user)

        return(False, "login failed")

class User(models.Model):
    full_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
