from django.shortcuts import render
import datetime

# Create your views here.
def template_view(request):
    date=datetime.datetime.now()
    name="vikas"
    th=int(date.strftime('%H'))
    if th<12:
        text="good morning"
    elif th<16:
        text="good afternoon"
    else:
        text="good night"
    dic={'date':date,'name':name,'text':text}
    return render(request,'template.html',dic)
