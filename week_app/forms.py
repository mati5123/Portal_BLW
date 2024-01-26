from django import forms
from .models import Died

class DiedForm(forms.ModelForm):
    class Meta:
        model = Died
        fields = ['text']