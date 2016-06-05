from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context 
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments, Category
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth 


def articles(request, page_number=1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 6)
    return render_to_response('articles.html', {'articles': current_page.page(page_number),'projects':Category.objects.all(),  'username': auth.get_user(request).username})



def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['projects']=Category.objects.all()
    args['article'] = Article.objects.get(id=article_id)
    args['category'] = Category.objects.filter(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)


def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            return_path = request.META.get('HTTP_REFERER','/')
            return redirect(return_path)
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
	    return_path = request.META.get('HTTP_REFERER','/')
	    response = redirect(return_path)
            response.set_cookie( article_id, "test")
            return response


    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
	    request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)


def articl_cat(request, category_id=1):
    args = {}
    args['projects']=Category.objects.all()
    args['category'] = Category.objects.get(id=category_id)
    args['articles'] = Article.objects.filter(category_id=category_id)
    args['username'] = auth.get_user(request).username

    branch_categories = args['category'].get_descendants(include_self=True)
    args['category_articles'] = Article .objects.filter(category__in=branch_categories).distinct()

    return render_to_response('articl_cat.html', args)



def stati(request, page_number=1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 6)
    return render_to_response('stati.html', {'articles': current_page.page(page_number),'projects':Category.objects.all(),  'username': auth.get_user(request).username})



