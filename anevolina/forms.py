from django import forms

class ConverterForm(forms.Form):
    class Meta:
        fields = ['recipe']

    recipe = forms.CharField(label='', widget=forms.Textarea())

