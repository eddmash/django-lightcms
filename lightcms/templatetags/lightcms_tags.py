from django import template
from django.conf import settings

from lightcms.models import Page

register = template.Library()


@register.inclusion_tag('lightcms/navs.html', takes_context=True)
def site_menu(context, domain='/pages/'):
    return {"pages": context.get('cms_menu_pages'), 'domain':domain}

@register.simple_tag(takes_context=True)
def cms_page_url(context, page):
    return