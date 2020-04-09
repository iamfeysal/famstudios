from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
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
    print(posts)
    data = {'posts': posts}
    return render(request, 'index.html', data)


def search_view(request):
    r_search = request.POST['search']
    posts = Post.objects.filter(
        Q(published=True) & (Q(title__icontains=r_search)
                             | Q(content__icontains=r_search))).order_by(
                             '-created_on')
    data = {'posts': posts}

    return render(request, 'search.html', data)
