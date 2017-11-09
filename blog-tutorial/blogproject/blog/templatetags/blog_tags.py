from ..models import Post, Category
from django import template
from django.utils.safestring import mark_safe
import markdown
register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
	return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.filter(name='markdown')
def markdown_format(text):
	return mark_safe(markdown.markdown(text,extensions=['markdown.extensions.extra','markdown.extensions.codehilite','markdown.extensions.toc',]))