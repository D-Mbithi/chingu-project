from django.utils.safestring import mark_safe
from django import template
import markdown

from blog.models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {
        'latest_posts': latest_posts
    }

@register.simple_tag
def featured_post():
    post = Post.published.order_by('-publish')[0]
    return post

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))