from django.urls import path, include, re_path
from .views import archive_view, post_detail, search_view, PostCategory, \
    PostListView, post_list

urlpatterns = [
    path('', post_list, name='home'),
    path('archive/', archive_view, name='archive'),
    path('post/<int:id>', post_detail, name='post_detail'),
    re_path(r'^post/cat/(?P<id>\d+)/$', PostCategory.as_view(),
            name='post_cat'),
    path('search_result/', search_view, name='search'),
]
