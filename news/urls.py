from django.urls import path, include
from .views import archive_view, post_detail, index, view_category, search_view

urlpatterns = [
    path('', index, name='home'),
    # path('post/cat', CategoryView.as_view(), name='category'),
    path('archive/', archive_view, name='archive'),
    path('post/<int:id>', post_detail, name='post_detail'),
    path('search_result/', search_view, name='search'),
]
