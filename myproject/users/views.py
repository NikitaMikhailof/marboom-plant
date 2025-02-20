from . models import Equipment
from django.views.generic import ListView


class PostListView(ListView):
    queryset = Equipment.objects.all()
    context_object_name = 'posts'
    template_name = 'users/index.html'
    extra_context = {
        'title': 'Главная страница',
    }
