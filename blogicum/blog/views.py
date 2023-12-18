from django.shortcuts import get_object_or_404, render

from .models import Category
from .querysets import FilteredQuerySet
from .utils import get_post_list


RECENT_POSTS_LIMIT = 5


def index(request):
    context = {
        'post_list': get_post_list()[:RECENT_POSTS_LIMIT],
    }
    template_name = 'blog/index.html'
    return render(request, template_name, context)


def post_detail(request, id):
    post = get_object_or_404(
        get_post_list(),
        id=id
    )
    context = {
        'post': post,
    }
    template_name = 'blog/detail.html'
    return render(request, template_name, context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        FilteredQuerySet(Category).is_published(),
        slug=category_slug
    )
    post_list = get_post_list().filter(category=category)
    context = {
        'category': category,
        'post_list': post_list
    }
    template_name = 'blog/category.html'
    return render(request, template_name, context)
