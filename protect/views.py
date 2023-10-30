from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.base import View
from .models import Post
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='author').exists()
        return context

class MyView(PermissionRequiredMixin, View):
    permission_required = ('<app>.<action>_<model>',
                           '<app>.<action>_<model>')


class CreatePostView(PermissionRequiredMixin, View):
    permission_required = 'newsapp.add_post'

    def get(self, request):
        if request.method == 'POST':

            form = PostForm(request.POST)
            if form.is_valid():

                post = form.save(commit=False)

                post.save()
                return redirect('post_list')
        else:

            form = PostForm()