from django import template
from django.conf import settings

from cms.models import Page

register = template.Library()


@register.inclusion_tag('cms/navs.html', takes_context=True)
def site_menu(context, domain='/pages/'):
    return {"pages": context.get('cms_menu_pages'), 'domain':domain}
