from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogPost


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'slug', 'content', 'preview', 'created_at', 'is_published')
    success_url = reverse_lazy('blog:blogpost_list')

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


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'slug', 'content', 'preview', 'created_at', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blogpost_view', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:blogpost_list')
