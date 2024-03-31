from django import template

register = template.Library()


@register.simple_tag
def my_media_tag(data):
    if data:
        return f'/media/{data}'
    return '#'
