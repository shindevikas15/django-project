from django.shortcuts import render
from webapp import forms

# Create your views here.

def login_view(request):
    return render (request,'myapp/login.html')

def fresher_view(request):
    form=forms.EmpFresherForm()
    if request.method=='POST':
        form=forms.EmpFresherForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("data successfuly entered")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['Email_ID'])

            print(form.cleaned_data['phone_number'])
            print(form.cleaned_data['location'])
            return thankviews(request)
    return render(request,'myapp/fresher.html',{'form':form})

    #return render (request,'myapp/fresher.html',{'form':form})
def professional_view(request):
    form=forms.EmpProfessionalForm()
    if request.method=='POST':
        form=forms.EmpProfessionalForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("data successfuly entered")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['Email_ID'])

            print(form.cleaned_data['phone_number'])
            print(form.cleaned_data['location'])
            return thankviews(request)
    return render(request,'myapp/professional.html',{'form':form})

def thankviews(request):
    return render(request, 'myapp/thanks.html')

    #return render (request,'myapp/professional.html',{'form':form})

