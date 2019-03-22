from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hits_view(request):
    hit=request.COOKIES.get('hit',0)
    newhit=int(hit)+1
    response=render(request,'myapp/welcome.html',{'hit':newhit})
    response.set_cookie('hit',newhit)
    return response
