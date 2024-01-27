from django import forms
from week_app.models import Died

class DiedForm(forms.ModelForm):
    class Meta:
        model = Died
        fields = ['text']
        text = forms.CharField(widget=forms.Textarea())

