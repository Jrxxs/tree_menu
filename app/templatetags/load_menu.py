from django import template
from django.utils.html import mark_safe
from ..models import Category


register = template.Library()

def make_tree(branch):
    content = ["<ul>"]

    for i in branch:
        content.append(f"<li><a href='/{i.id}'>{i.name}</a></li>")
        if not branch[i] is None:
            content.append(make_tree(branch[i]))

    content.append("</ul>")
    content = "".join(content)
    return content


@register.simple_tag()
def draw_menu(name: str):

    menu = list(Category.objects.select_related('parent').all())

    obj = list(filter(lambda x: x.name == name, menu))[0]
    childs = dict.fromkeys(list(filter(lambda x: x.parent == obj, menu)), None)
    
    while not obj.parent is None:
        parent = list(filter(lambda x: x == obj.parent, menu))[0]
        siblings = dict.fromkeys(list(filter(lambda x: x.parent == parent, menu)), None)
        siblings[obj] = childs
        childs = siblings
        obj = parent

    siblings = list(filter(lambda x: x.parent is None, menu))
    
    content = [""]
    for i in siblings:
        content.append(f"<li><a href='/{i.id}'>{i.name}</a></li>")
        if i is obj:
            content.append(make_tree(childs))

    content = "".join(content)
    
    return mark_safe(content)