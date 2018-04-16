from django import forms
from . import models
from .fields import ModelChoiceField

__author__ = 'eddmash'


class CreatePageForm(forms.ModelForm):
    class Meta:
        model = models.Page
        fields = ['title', 'content', 'publish', 'parent', 'order']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'wysihtml5-editor editor'})
        }
        field_classes={
            'parent': ModelChoiceField
        }
