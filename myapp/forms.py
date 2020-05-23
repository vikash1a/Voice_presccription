
from django import forms

from myapp.models import prescription

class prescriptionForm(forms.ModelForm):
    class Meta:
        model=prescription
        fields=('name','symptoms','diagnosis','pescription','advice')