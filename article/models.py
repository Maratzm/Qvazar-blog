# -*- coding: utf-8 -*-
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import mptt
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.

class Category(MPTTModel):
    class Meta():
        db_table = 'category'
        verbose_name_plural = "Категории"
        verbose_name = "Категория"
        ordering = ('tree_id','level')

    name = models.CharField(max_length=150,verbose_name="Категория")
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u'РОДИТЕЛЬСКИЙ класс')

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_py = ['name']

mptt.register(Category, order_insertion_by=['name'])


class Article(models.Model):
    class Meta():
        db_table = 'article'

    article_title = models.CharField(max_length=200)
    article_anot = models.CharField(max_length=100, default='')
    article_text = RichTextUploadingField(blank=True, default='')
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)
    category = TreeForeignKey(Category,  blank=True, null=True, related_name='cat')

class Comments(models.Model):
    class Meta():
        db_table = 'comments'
    comments_text = models.TextField(verbose_name="Текст комментария")
    comments_article = models.ForeignKey(Article)

