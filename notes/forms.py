from django import forms

from .models import Notes

from pagedown.widgets import PagedownWidget

class NotesForm(forms.ModelForm):
    body = forms.CharField( widget = PagedownWidget)

    class Meta:
        model = Notes
        fields = '__all__'


