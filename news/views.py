from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post, Category
from django.db.models import Q


def latest_view(request):
    posts = Post.published.all()
    data = {'posts': posts, }
    return render(request, 'index.html', data)


def post_detail(request, id):
    posts = Post.objects.get(id=id)
    data = {'posts': posts}
    return render(request, 'post_detail.html', data)


def post_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category__slug=category_slug)
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/post_by_category.html', context)


# view function to display post by tag
def post_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags__name=tag)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/post_by_tag.html', context)


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
