from django.shortcuts import render
from webapp import forms

# Create your views here.
def student_view(request):
    form=forms.studentform()
    my_dict={'form':form}
    return render(request,'myapp/welcome.html',my_dict)
