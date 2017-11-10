# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    #list of post
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # passing those posts to template, put into {}
    return render(request, 'blog/post_list.html', {'posts': posts})
