from django.shortcuts import render
from .models import  Equipment, Journal, Comments
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchForm, JournalForm, CommentForm
from django.views.generic.edit import FormMixin


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


class JournalListView(LoginRequiredMixin, ListView):
    model = Journal
    paginate_by = 10 
    template_name = 'users/journal.html'
    context_object_name = 'records'

    def get_queryset(self):
        return Journal.objects.prefetch_related('equipment').all()


class CommentListView(LoginRequiredMixin, ListView):
    model = Comments
    paginate_by = 10 
    template_name = 'users/comment.html'
    context_object_name = 'records'

    def get_queryset(self):
        return Comments.objects.prefetch_related('equipment').all()


class ShowDetailEquipment(LoginRequiredMixin, DetailView):
    model = Equipment
    slug_url_kwarg = 'post_slug'
    template_name = 'users/detail.html'
    context_object_name = 'equipment'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journals'] = Journal.objects.prefetch_related('equipment').filter(equipment__slug=self.kwargs['post_slug'])
        context['comments'] = Comments.objects.prefetch_related('equipment').filter(equipment__slug=self.kwargs['post_slug'])
        return context
    

class JournalRecordsEquipment(LoginRequiredMixin, ListView):
    model = Equipment
    paginate_by = 10
    slug_url_kwarg = 'equipment_slug'
    template_name = 'users/journal_equipment_records.html'
    context_object_name = 'records'
    
    def get_queryset(self):
        records = Journal.objects.prefetch_related('equipment').filter(equipment__slug=self.kwargs['equipment_slug'])
        return records


class CommentRecordsEquipment(LoginRequiredMixin, ListView):
    model = Equipment
    paginate_by = 10
    slug_url_kwarg = 'equipment_slug'
    template_name = 'users/comment_equipment_records.html'
    context_object_name = 'records'
    
    def get_queryset(self):
        records = Comments.objects.prefetch_related('equipment').filter(equipment__slug=self.kwargs['comment_slug'])
        return records


def journal_record(request):
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = JournalForm()       
         
    return render(request,
                'users/record_successfully.html',
                {'form': form,
                 'title': 'Запись успешна сохранена в журнале'
                })   


def comment_record(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()       
         
    return render(request,
                'users/record_successfully.html',
                {'form': form,
                 'title': 'Комментарий успешно сохранен'
                })   


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


def search_journal(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Journal.objects.filter(equipment__title__icontains=query)
            total = results.count()
    else:
        form = SearchForm()       
         
    return render(request,
                'users/journal_search.html',
                {'form': form,
                'posts': results,
                'total': total
                })  


def search_journal(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Comments.objects.filter(equipment__title__icontains=query)
            total = results.count()
    else:
        form = SearchForm()       
         
    return render(request,
                'users/comment_search.html',
                {'form': form,
                'posts': results,
                'total': total
                })  