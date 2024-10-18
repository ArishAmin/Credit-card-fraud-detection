# myapp/forms.py
from django import forms

class TransactionForm(forms.Form):
    amount = forms.FloatField(label='Transaction Amount', min_value=0.0)
    time = forms.IntegerField(label='Transaction Time (in seconds)', min_value=0)
