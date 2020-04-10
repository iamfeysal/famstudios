from django.urls import path, include
from .views import archive_view, post_detail, HomeView, search_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('archive/', archive_view, name='archive'),
    path('post/<int:id>', post_detail, name='post_detail'),
    url(r'^category$', views.category_list, name='category_list'),
    url(r'^category/(?P<pk>\d+)/$', views.category_detail,
        name='category_detail'),
    path('search_result/', search_view, name='search'),
]
