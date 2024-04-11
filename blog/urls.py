from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogPostListView, BlogPostDetailView, BlogPostCreateView, BlogPostUpdateView, \
    BlogPostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('view/<str:slug>/', BlogPostDetailView.as_view(), name='blogpost_view'),
    path('edit/<int:pk>/', BlogPostUpdateView.as_view(), name='blogpost_edit'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='blogpost_delete')
]
