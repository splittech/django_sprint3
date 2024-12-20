from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone
from .models import Post, Category


# Create your views here.
def index(request):
    template_name = 'blog/index.html'

    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[0:5]

    context = {
        'post_list': post_list
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'blog/detail.html'

    post = get_object_or_404(Post, pk=post_id)

    if post.pub_date > timezone.now():
        raise Http404

    if not post.is_published:
        raise Http404

    if not post.category.is_published:
        raise Http404

    context = {
        'post': post
    }

    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'

    category = Category.objects.values(
        'id',
        'title',
        'description',
        'is_published'
    ).get(slug=category_slug)

    if not category['is_published']:
        raise Http404()

    post_list = Post.objects.filter(
        category=category['id'],
        pub_date__lte=timezone.now(),
        is_published=True,
    ).order_by('-pub_date')

    context = {
        'category': category,
        'post_list': post_list
    }

    return render(request, template_name, context)
