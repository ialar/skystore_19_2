from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import BlogPostForm
from blog.models import BlogPost

CONTENT_PERMISSIONS = ('blog.can_change_blogpost_title', 'blog.can_change_blogpost_content',
                       'blog.can_change_blogpost_preview', 'blog.can_change_blogpost_is_published_status')


class BlogPostCreateView(PermissionRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:blogpost_list')
    permission_required = CONTENT_PERMISSIONS

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
        return super().form_valid(form)


class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogPostUpdateView(PermissionRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:blogpost_list')
    permission_required = CONTENT_PERMISSIONS


class BlogPostDeleteView(PermissionRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:blogpost_list')
    permission_required = CONTENT_PERMISSIONS
