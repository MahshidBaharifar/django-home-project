from django import forms

class PostForm(forms.Form):
    title = forms.CharField()
    text = forms.TextInput()
    is_enable = forms.BooleanField()
    published_date = forms.DateField()
    created_time = forms.DateTimeField()
    updated_time = forms.DateTimeField()