from django import forms

class AddUrlForm(forms.Form):
    url_link = forms.CharField(max_length=128)
    word = forms.CharField(max_length=64)
