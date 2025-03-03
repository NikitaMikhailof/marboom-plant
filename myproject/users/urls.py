from django.urls import path, re_path
from . import views 


urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('show_posts/<slug:cat_slug>/', views.CategoryListView.as_view(), name='show_category'),
    path('show_tags/<slug:tag_slug>/', views.TagListView.as_view() , name='show_tag'),
]

