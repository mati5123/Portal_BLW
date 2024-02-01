from django import forms
from week_app.models import Died, Comment, Image

class DiedForm(forms.ModelForm):
    class Meta:
        model = Died
        fields = ['id','text', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        text = forms.CharField(widget=forms.Textarea())

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']


