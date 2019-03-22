from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test_cookie(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>heii cookies u r testing<h1>")
def check_cookie(request):
    if request.session.test_cookie_worked():
        print("cookies are wroking properly")
        request.session.delete_test_cookie()
        return HttpResponse("<h1>good bye cookies u r deleted<h1>")
