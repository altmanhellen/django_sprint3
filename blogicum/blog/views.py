from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


RECENT_POSTS_LIMIT = 5


def published_recent_posts(category=None):
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
    if category:
        posts = posts.filter(category=category)
    return posts


def index(request):
    template_name = 'blog/index.html'
    post_list = published_recent_posts()
    context = {
        'post_list': post_list[:RECENT_POSTS_LIMIT],
    }
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post_list = published_recent_posts()
    post = get_object_or_404(
        post_list,
        id=id
    )
    context = {
        'post': post,
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = published_recent_posts(category=category)
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template_name, context)
