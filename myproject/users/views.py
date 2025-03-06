from django.shortcuts import render
from .models import  Equipment, Journal
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchForm


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


class ShowDetailEquipment(LoginRequiredMixin, DetailView):
    model = Equipment
    slug_url_kwarg = 'post_slug'
    template_name = 'users/detail.html'
    context_object_name = 'equipment'

    def get_queryset(self):
        return Equipment.objects.prefetch_related('journals').filter(slug=self.kwargs['post_slug'])
    
    


def search_equipment(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Equipment.objects.filter(title__icontains=query)
            total = results.count()
    else:
        form = SearchForm()       
         
    return render(request,
                'users/search_result.html',
                {'form': form,
                'posts': results,
                'total': total
                })        