from django import forms
from .models import Congratulation

class CongratulationForm(forms.ModelForm):
    class Meta:
        model = Congratulation
        fields = ['name', 'message']