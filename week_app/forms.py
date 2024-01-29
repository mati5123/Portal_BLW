from django import forms
from week_app.models import Died, Comment

class DiedForm(forms.ModelForm):
    class Meta:
        model = Died
        name = forms.CharField(max_length=64)
        fields = ['text']
        text = forms.CharField(widget=forms.Textarea())

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        text = forms.CharField(widget=forms.Textarea())
