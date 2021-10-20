from django.core.paginator import Paginator
from django.shortcuts import render

from news.models import New, Tag


def index(request):
    news = New.objects.all()
    paginator = Paginator(news, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'title': 'NEWS', 'page_obj': page_obj}
    return render(request, 'news/index.html', context)


def new_page(request, new_id, ):
    new = New.objects.filter(id=new_id)[0]
    new.counter_of_viewing += 1
    new.save()
    context = {'title': new.header, 'new': new}
    return render(request, 'news/new.html', context)


def news_by_tag(request, tag_id):
    tag = Tag.objects.filter(id=tag_id)[0]
    news = New.objects.filter(tags=tag)
    paginator = Paginator(news, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'title': tag.tag_name, 'page_obj': page_obj}
    return render(request, 'news/news by tag.html', context)


def statistic_of_views(request):
    news = New.objects.order_by('-counter_of_viewing')
    context = {'title': 'Статистика', 'news': news}
    return render(request, 'news/statistic.html', context)
