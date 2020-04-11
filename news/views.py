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
    category_list_count = Post.objects.annotate(num_category=Count('category'))
    # category_list_count = Post.objects.annotate(num_category=Count(
    # 'category'))

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
        'category_list_count': category_list_count,
    }
    return render(request, "index.html", context)


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

# class HomeView(ListView):
#     template_name = 'index.html'
#     model = Category
#     context_object_name = 'all_categs'
#
#     def get_queryset(self):
#         return Category.objects.all()
#
#     def get_context_data(self):
#         context = super(HomeView, self).get_context_data()
#         context['posts'] = Post.published.all()
#         # This will show your 3 latest posts you can add accordingly
#         return context

# class HomeView(ListView):
#     template_name = 'index.html'
#     model = Post
#
#     # context_object_name = 'all_categs'
#
#     def get_queryset(self):
#         self.category = get_object_or_404(Category)
#         posts = Post.published.all()
#         print(posts)
#         return posts.filter(category=self.category)
#
#     def get_context_data(self,**kwargs):
#         context = super(HomeView, self).get_context_data(**kwargs)
#         context['posts'] = Post.published.all()
#         # This will show your 3 latest posts you can add accordingly
#         return context
