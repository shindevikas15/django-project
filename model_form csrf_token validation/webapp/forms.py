from django import forms

class studentform(forms.Form):
    name=forms.CharField()
    fees=forms.IntegerField()