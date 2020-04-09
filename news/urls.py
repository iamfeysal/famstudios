from django.urls import path, include
from .views import archive_view, post_detail, latest_view, search_view

urlpatterns = [
    path('', latest_view, name='home'),
    path('archive/', archive_view, name='archive'),
    path('post/<int:id>', post_detail, name='post_detail'),
    path('search_result/', search_view, name='search'),
]
