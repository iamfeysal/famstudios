from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Category
from django.db.models import Q


def archive_view(request):
    posts = Post.published.all()
    data = {'posts': posts}
    return render(request, 'archive.html', data)


def post_detail(request, id):
    posts = Post.objects.get(id=id)
    data = {'posts': posts}
    return render(request, 'post_detail.html', data)


def latest_view(request):
    posts = Post.published.all()
    categories = Category.objects.all()
    print(categories)
    data = {'posts': posts, 'categories': categories}
    return render(request, 'index.html', data)


def search_view(request):
    r_search = request.POST['search']
    posts = Post.objects.filter(Q(
            title__icontains=r_search) | Q(
            slug__icontains=r_search) | Q(
            description__icontains=r_search)
                                )
    data = {'posts': posts}

    return render(request, 'search.html', data)
