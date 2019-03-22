from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from webapp.forms import signupForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_page(request):
    return render(request,'myapp/home.html')
@login_required
def customer(request):
    return render(request,'myapp/customer.html')
def logout(request):
    return render(request,'myapp/logout.html')

def registration_view(request):
    form=signupForm()
    if request.method=='POST':
        form=signupForm(request.POST)
        user=form.save(commit=True)
        user.set_password(user.password)
        user.save()

        return HttpResponseRedirect('/accounts/login')
    return render(request,"myapp/registration.html",{'form':form})