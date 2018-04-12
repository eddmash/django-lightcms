from django import forms
from cms import models
from errand import helpers

__author__ = 'eddmash'


class CreatePageForm(helpers.BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = models.Page
        fields = ['title', 'content', 'publish', 'parent', 'order']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'wysihtml5-editor editor'})
        }
