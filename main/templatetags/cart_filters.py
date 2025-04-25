from django import template

register = template.Library()

@register.filter
def get_item(cart, book_id):
    return cart.get(str(book_id), 0)
