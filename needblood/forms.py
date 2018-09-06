from django import forms
from .models import Receiver


class ReceiverForm(forms.ModelForm):


    class Meta:
        model = Receiver
        fields = ['receiver', 'blood_group', 'mobile_no', 'email','hospital','city']
