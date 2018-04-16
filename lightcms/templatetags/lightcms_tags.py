from django import template
from django.conf import settings

from lightcms.models import Page
from lightcms.helper import page_breadcrumb

register = template.Library()


@register.inclusion_tag('lightcms/navs.html', takes_context=True)
def site_menu(context, domain='/pages/'):
    return {"pages": context.get('cms_menu_pages'), 'domain': domain}


@register.filter
def cms_page_breadcrumb(page, as_list=False, separator=" > "):
    """
    Return the hierarchy of a page, i.e, returns all the parent of a page if it has any
    :param page: the page we get the hierarchy for.
    :param as_list: if true we return a list of the page titles else return a string
    separated by separator
    :param separator: the separator to use default to >
    :return:
    """
    return page_breadcrumb(page, as_list, separator)
