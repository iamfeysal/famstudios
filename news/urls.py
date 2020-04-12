from django.urls import path, include, re_path
from .views import archive_view, post_detail, search_view, post_list, \
    list_of_post_by_category

urlpatterns = [
    path('', post_list, name='home'),
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', post_list,
            name='post_list_by_tag'),
    re_path(r'^category/(?P<category_slug>[-\w]+)/$', list_of_post_by_category,
            name='list_of_post_by_category'),
    path('archive/', archive_view, name='archive'),
    path('post/<int:id>', post_detail, name='post_detail'),
    path('search_result/', search_view, name='search')
]
