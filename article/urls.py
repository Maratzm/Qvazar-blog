# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'firstapp.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                    url(r'^articles/all/$', 'article.views.articles'),
		    url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
		    url(r'^articles/addlike/(?P<article_id>\d+)/$', 'article.views.addlike'),
		    url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
                    url(r'^page/(\d+)/$', 'article.views.articles'),
		    url(r'^category/get/(?P<category_id>\d+)/$', 'article.views.articl_cat'),
		    url(r'^stati/', 'article.views.stati'),
		    url(r'^$', 'article.views.articles'),

)	

