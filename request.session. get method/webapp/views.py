from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hits_view(request):
    hit=request.session.get('hit',0)
    newhit=int(hit)+1
    request.session ['hit']=newhit
    return render(request,'myapp/welcome.html',{'hit':newhit})

