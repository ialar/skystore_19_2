from blog.models import BlogPost
from catalog.forms import StyleFormMixin


class BlogPostForm(StyleFormMixin):
    class Meta:
        model = BlogPost
        exclude = ('slug', 'views',)
