from django import forms
from .models import Doner


class RegisterForm(forms.ModelForm):


    class Meta:
        model = Doner
        fields = ['doner', 'blood_group', 'mobile_no', 'email','city']
