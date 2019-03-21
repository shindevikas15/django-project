from django import forms
from webapp.models import EmpFresher
from webapp.models import EmpProfessional



#fields with validations
class EmpFresherForm(forms.ModelForm):
    class Meta :
        model=EmpFresher
        fields='__all__'

class EmpProfessionalForm(forms.ModelForm):
    class Meta :
        model=EmpProfessional
        fields='__all__'