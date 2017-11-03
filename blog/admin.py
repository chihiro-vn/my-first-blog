# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post

# Register your models here.
# include the model Post from models.py file
admin.site.register(Post)