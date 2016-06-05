# -*- coding: utf-8 -*-
from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from article.models import Article, Comments
from article.models import  Category


# Register your models here.
class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_anot', 'article_text', 'article_date','category']
    list_display= ['article_title', 'article_date', 'category']
    inlines = [ArticleInline]
    list_filter = ['article_date']
    search_fields = ['article_title']

class CategoryAdmin(admin.ModelAdmin):
    fields =  ['name', 'parent']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
