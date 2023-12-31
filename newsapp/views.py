from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post
from datetime import datetime
from .filters import PostFilter
from django.urls import reverse_lazy
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

class PostList(ListView):
    model = Post
    ordering = ['name']
    template_name = 'flatpages/post.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()

        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_news'] = None
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post_detail.html'
    context_object_name = 'posts'

    def post_detail(request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'post_detail.html', {'post': post})

class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'flatpages/post_edit.html'
    def form_valid(self, form):
        news = form.save(commit=False)
        news.post_type = 'NW'
        news.save()
        return super().form_valid(form)
class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'flatpages/post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'flatpages/post_delete.html'
    success_url = reverse_lazy('post_list')


class PostSearch(ListView):
    model = Post
    template_name = 'flatpages/post_search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/articles_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.post_type = 'AR'
        news.save()
        return super().form_valid(form)

class ArticlesUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/post_edit.html'



class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'flatpages/articles_delete.html'
    success_url = reverse_lazy('post_list')
