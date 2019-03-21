from django import forms

class studentform(forms.Form):
    name=forms.CharField()
    fees=forms.FloatField()
    email=forms.EmailField()
    address=forms.CharField()
