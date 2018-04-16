def page_breadcrumb(page, as_list=False, separator=" > "):
    """
    Return the hierarchy of a page, i.e, returns all the parent of a page if it has any
    :param page: the page we get the hierarchy for.
    :param as_list: if true we return a list of the page titles else return a string
    separated by separator
    :param separator: the separator to use default to >
    :return:
    """
    has_parent = lambda page: True if page.parent else False

    title = [page.title]
    while has_parent(page):
        title.insert(0, page.parent.title)
        page = page.parent

    if not as_list:
        title = separator.join(title)
    return title