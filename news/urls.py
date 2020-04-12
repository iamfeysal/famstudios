from django.urls import path, include, re_path
from .views import archive_view, post_detail, search_view, post_list,\
    categories_m

urlpatterns = [
    path('', post_list, name='home'),
    re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', post_list,
            name='post_list_by_tag'),
    path('category/<int:pk>', categories_m,
         name='postcategory'),
    path('archive/', archive_view, name='archive'),
    path('post/<int:id>', post_detail, name='post_detail'),
    path('search_result/', search_view, name='search')
]
