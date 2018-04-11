from django.conf import settings
from django.db import models
from django.db.models import Prefetch
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as __

from errand import fields

PAGE_TYPE = "PAGE"
PUBLISH = "PUBLISH"
DRAFT = "DRAFT"
POST_TYPES = (
    (PAGE_TYPE, "Page"),
)
POST_STATUS = (
    (DRAFT, "Draft"),
    (PUBLISH, "Publish"),
)


class Page(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(app_label)s_%(class)s_author')
    title = models.CharField(max_length=40)
    content = models.TextField()
    order = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=25, default=PAGE_TYPE, choices=POST_TYPES)
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name=__("Parent Page"))
    publish = models.CharField(max_length=25, default=DRAFT, choices=POST_STATUS)
    slug = fields.SlugField(field='title')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='%(app_label)s_%(class)s_last_modified_by', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("cms:page-edit", args=[str(self.slug)])

    def has_submenu(self):
        return self.page_set.exists()

    @classmethod
    def get_menu_pages(cls):
        return cls.objects.filter(publish=PUBLISH, parent__isnull=True).order_by('order').prefetch_related(
            Prefetch('page_set', queryset=cls.objects.filter(publish=PUBLISH, parent__isnull=False).order_by('order')))
