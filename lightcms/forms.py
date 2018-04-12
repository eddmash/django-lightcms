from django import forms
from . import models

__author__ = 'eddmash'


class CreatePageForm(forms.ModelForm):
    class Meta:
        model = models.Page
        fields = ['title', 'content', 'publish', 'parent', 'order']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'wysihtml5-editor editor'})
        }
