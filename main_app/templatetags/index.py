from django import template

register = template.Library()

@register.filter
def index(idx,i):
    return idx[i]