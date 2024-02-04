from django import forms
from week_app.models import Died, Comment, Image
from django.forms.widgets import ClearableFileInput

class DiedForm(forms.ModelForm):
    class Meta:

        model = Died
        fields = ['id','text', 'image']
        labels = {
            'text': '',
            'image': '',

        }
        widgets = {
            'image': forms.ClearableFileInput(attrs={'clear-image': 'lalala'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
        labels = {
            'text': '',
        }
        text = forms.CharField(widget=forms.Textarea())


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        labels = {
            'image': '',
        }

