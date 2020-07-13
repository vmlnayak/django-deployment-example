from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    Thiscuts all values of arg from the string
    """

    return value.replace(arg,'')

# register.filter('cut',cut)
