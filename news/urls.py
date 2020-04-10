from django.urls import path, include, re_path
from .views import archive_view, post_detail, search_view, latest_view

urlpatterns = [
    path('', latest_view, name='home'),
    path('archive/', archive_view, name='archive'),
    path('post/<int:id>', post_detail, name='post_detail'),
    # re_path(r'^category$', category_list, name='category_list'),
    # re_path(r'^category/(?P<pk>\d+)/$', category_detail,
    #         name='category_detail'),
    path('search_result/', search_view, name='search'),
]
