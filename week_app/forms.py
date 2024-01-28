from django import forms
from week_app.models import Died, Comment

class DiedForm(forms.ModelForm):
    class Meta:
        model = Died
        fields = ['text']
        text = forms.CharField(widget=forms.Textarea())

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        content = forms.CharField(widget=forms.Textarea())
