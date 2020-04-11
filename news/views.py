from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post, Category
from django.db.models import Q, Count


# def latest_view(request):
#     posts = Post.published.all()
#     data = {'posts': posts, }
#     return render(request, 'index.html', data)

class PostListView(ListView):
    model = Category
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        posts = Post.published.all()
        posts = (
            posts.objects.filter(category=self.category)
        )
        context['posts'] = posts
        return context


def post_detail(request, id):
    posts = Post.objects.get(id=id)
    data = {'posts': posts}
    return render(request, 'post_detail.html', data)


# class PostCategory(ListView):
#     model = Post
#     template_name = 'index.html'
#
#     def get_queryset(self):
#         post_cat = Post.published.all()
#         self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
#         return post_cat.filter(category=self.category)
#
#     def get_context_data(self, **kwargs):
#         context = super(PostCategory, self).get_context_data(**kwargs)
#         context['category'] = self.category
#         return context

def post_list(request):
    object_list = Post.objects.filter(status='Published').order_by("-created")
    recent_post = object_list[:4]
    category_list_count = Post.objects.annotate(num_category=Count('Category'))

    context = {
        'recent_post': recent_post,
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
