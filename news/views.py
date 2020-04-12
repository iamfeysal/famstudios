from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from taggit.models import Tag

from .models import Post, Category
from django.db.models import Q, Count


def post_detail(request, id):
    posts = Post.objects.get(id=id)
    data = {'posts': posts}
    return render(request, 'post_detail.html', data)


def post_list(request, tag_slug=None):
    posts = Post.published.all()
    categories = Category.objects.all()
    print(categories)
    postcat = posts.filter(category=categories)
    # category_list_count = Post.objects.annotate(num_category=Count(
    #     'category'))

    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    # paginator = Paginator(posts, 10)  # 3 posts in each page
    # page = request.GET.get('page')
    #
    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer deliver the first page
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range deliver last page of results
    #     posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'tag': tag,
        'postcat': postcat,
        'categories':categories
        # 'category_list_count': category_list_count,
    }
    return render(request, "index.html", context)


def list_of_post_by_category(request, slug):
    categories = Category.objects.all()
    print(categories)
    post = Post.published.all()
    post = post.filter(category=categories)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        post = post.filter(category=category)
        # print(post)
    context = {
        'categories': categories,
        'postcat': post,
    }
    return render(request, "category.html", context)


def archive_view(request):
    posts = Post.published.all()
    data = {'posts': posts}
    return render(request, 'archive.html', data)


def search_view(request):
    r_search = request.POST['search']
    posts = Post.objects.filter(Q(
        title__icontains=r_search) | Q(
        slug__icontains=r_search) | Q(
        description__icontains=r_search)
                                )
    data = {'posts': posts}

    return render(request, 'search.html', data)
