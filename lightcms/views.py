from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from cms import forms
from errand import helpers
from . import models


class PageCreateView(helpers.AdminMixin, generic.CreateView):
    model = models.Page
    template_name = "cms/page/create.html"
    form_class = forms.CreatePageForm
    back_url = reverse_lazy("cms:pages")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.modified_by = self.request.user
        return super(PageCreateView, self).form_valid(form)


class PageUpdateView(helpers.AdminMixin, generic.UpdateView):
    model = models.Page
    template_name = "cms/page/create.html"
    form_class = forms.CreatePageForm
    success_url = back_url = reverse_lazy("cms:pages")

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        return super(PageUpdateView, self).form_valid(form)


class PageListView(helpers.AdminMixin, generic.ListView):
    model = models.Page
    back_url = reverse_lazy("inventory:home")
    template_name = "cms/page/list.html"
