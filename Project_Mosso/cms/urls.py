# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from cms import views

urlpatterns = patterns('',
    url(r'^book/$', views.book_list, name='book_list'),   
    url(r'^book/add/$', views.book_edit, name='book_add'),  
    url(r'^book/mod/(?P<book_id>\d+)/$', views.book_edit, name='book_mod'),  
    url(r'^book/del/(?P<book_id>\d+)/$', views.book_del, name='book_del'),
)