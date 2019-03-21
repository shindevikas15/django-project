from django.shortcuts import render
from webapp import forms

# Create your views here.
def thankviews(request):
    return render(request,'myapp/thanks.html')
def student_view(request):
    form=forms.studentform()
    if request.method=='GET':
        form=forms.studentform()
        return render(request, 'myapp/welcome.html', {'form': form})
    if request.method == 'POST':
        form = forms.studentform(request.POST)
        if form.is_valid():
            print("validation are success...!!")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])

            print(form.cleaned_data['fees'])
            print(form.cleaned_data['address'])
            return thankviews(request)



