from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from . import forms
from . import models


class PageCreateView(generic.CreateView):
    model = models.Page
    template_name = "lightcms/page/create.html"
    form_class = forms.CreatePageForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.modified_by = self.request.user
        return super(PageCreateView, self).form_valid(form)


class PageUpdateView(generic.UpdateView):
    model = models.Page
    template_name = "lightcms/page/create.html"
    form_class = forms.CreatePageForm

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        return super(PageUpdateView, self).form_valid(form)


class PageListView(generic.ListView):
    model = models.Page
    template_name = "lightcms/page/list.html"

    def get_queryset(self):
        self.queryset = self.model.objects.select_related('parent')
        return super().get_queryset()



