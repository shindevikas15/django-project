from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hits_view(request):
    hit=request.session.get('hit',0)
    newhit=int(hit)+1
    request.session ['hit']=newhit
    print("session expired age:",request.session.get_expiry_age())
    print("session expired date:", request.session.get_expiry_date())

    return render(request,'myapp/welcome.html',{'hit':newhit})

