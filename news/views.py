from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post, Category
from django.db.models import Q


def index(request):
    posts = Post.published.all()
    categories = Category.objects.all(),
    return render('index.html', {
        'categories': categories,
        'posts': posts
    })


def show_category(request, hierarchy=None):
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [x.slug for x in category_queryset]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category, slug=slug, parent=parent)
        else:
            instance = get_object_or_404(Post, slug=slug)
            breadcrumbs_link = instance.get_cat_list()
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in
                             breadcrumbs_link]
            breadcrumbs = zip(breadcrumbs_link, category_name)
            return render(request, "postDetail.html",
                          {'instance': instance, 'breadcrumbs': breadcrumbs})

    return render(request, "categories.html",
                  {'post_set': parent.post_set.all(),
                   'sub_categories': parent.children.all()})


# def view_post(request, slug):
#     return render('view_post.html', {
#         'post': get_object_or_404(Post, slug=slug)
#     })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.published.all()
    return render('index.html', {
        'category': category,
        'posts': posts.filter(category=category)
    })


def archive_view(request):
    posts = Post.published.all()
    data = {'posts': posts}
    return render(request, 'archive.html', data)


def post_detail(request, id):
    posts = Post.objects.get(id=id)
    data = {'posts': posts}
    return render(request, 'post_detail.html', data)


# def latest_view(request):
#     posts = Post.published.all()
#     categories = Category.objects.all()
#     print(categories)
#     data = {'posts': posts, 'categories': categories}
#     return render(request, 'index.html', data)

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


def search_view(request):
    r_search = request.POST['search']
    posts = Post.objects.filter(Q(
        title__icontains=r_search) | Q(
        slug__icontains=r_search) | Q(
        description__icontains=r_search)
                                )
    data = {'posts': posts}

    return render(request, 'search.html', data)
