from django import forms
from .models import Signal

class SignalForm(forms.ModelForm):
    class Meta:
        model = Signal
        fields =[ 'name', 'age', 'complexion','job']