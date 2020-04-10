from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post, Category
from django.db.models import Q


# def latest_view(request):
#     posts = Post.published.all()
#     data = {'posts': posts, }
#     return render(request, 'index.html', data)

class PostListView(DetailView):
    model = Category
    template_name = 'index.html'

    def get_queryset(self):
        post_cat = Post.published.all()
        self.posts = get_object_or_404(Post, pk=self.kwargs['pk'])
        return post_cat.filter(category=self.posts)

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['posts'] = self.posts
        return context
class PostCategory(ListView):
    model = Post
    template_name = 'index.html'

    def get_queryset(self):
        post_cat = Post.published.all()
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return post_cat.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(PostCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context

def post_detail(request, id):
    posts = Post.objects.get(id=id)
    data = {'posts': posts}
    return render(request, 'post_detail.html', data)





# def category_list(request):
#     categories_list = Category.objects.all()  # this will get all categories,
#     # you
#     # can do some filtering if you need (e.g. excluding categories without
#     # posts in it)
#
#     return render(request, 'index.html', {
#         'categories_list': categories_list})  # blog/category_list.html
#     # should be the
#     # template that categories are listed.
#
#
# def category_detail(request, pk):
#     categorys_detail = get_object_or_404(Category, pk=pk)
#     return render(request, 'index.html', {
#         'categorys_detail': categorys_detail})  # in this template, you will
#     # have access to
#     # category and posts under that category by (category.post_set).


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
