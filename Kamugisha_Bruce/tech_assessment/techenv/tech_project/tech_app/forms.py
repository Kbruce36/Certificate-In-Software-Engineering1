from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['firstname', 'lastname', 'date_of_birth',
                   'gender', 'country', 'state_district',
                     'town', 'zipcode', 'phone1', 'phone2',
                       'email']
