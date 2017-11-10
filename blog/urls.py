"""

"""
from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #r beginning
    # ^post/: after beginning
    # (\d+) : pattern digit repeat
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
