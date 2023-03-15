from django import forms

from .models import Data


class Create_data(forms.ModelForm):
    class Meta:
        model = Data
        fields = (
                'description',
        )


class Application_accomodation(forms.Form):
    description = forms.CharField()
