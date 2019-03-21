from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page(request):
    return render(request,'myapp/home.html')
@login_required
def customer(request):
    return render(request,'myapp/customer.html')
