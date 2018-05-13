from django import forms
from temperature.models import Temperature


class TemperatureForm (forms.ModelForm):
    class Meta:
        model = Temperature
        fields = ('temperature', 'min_temp', 'max_temp')


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
 
