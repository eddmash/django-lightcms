from cms.models import Page


def menu_pages(request):
    return {'cms_menu_pages': Page.get_menu_pages()}