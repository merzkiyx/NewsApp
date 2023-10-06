from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime

class PostList(ListView):

    model = Post
    ordering = ['name']
    template_name = 'flatpages/post.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_news'] = None
        return context

class PostDetail(DetailView):

    model = Post
    template_name = 'flatpages/post_detail.html'
    context_object_name = 'posts'

    def post_detail(request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        return render(request, 'post_detail.html', {'post': post})