from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import get_user_model, Equipment, Category, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(LoginRequiredMixin,ListView):
    queryset = Equipment.objects.all()
    total = queryset.count()
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'users/index.html'

    extra_context = {
        'total': total
    }


class CategoryListView(LoginRequiredMixin, ListView):
    model = Equipment
    paginate_by = 6
    template_name = 'users/show_categories.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Equipment.objects.filter(cat__slug=self.kwargs['cat_slug'])
    


class TagListView(LoginRequiredMixin, ListView):
    model = Equipment
    paginate_by = 6
    template_name = 'users/show_categories.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Equipment.objects.filter(tags__slug=self.kwargs['tag_slug'])

