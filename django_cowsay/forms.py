from django import forms

from django_cowsay.models import CowsayInputModel


class CowsayForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput, max_length=100)