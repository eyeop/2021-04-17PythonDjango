from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "index.html", {})
    # return HttpResponse("<h1>Welcome to Jaewon's First Site!</h1>")


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page!</h1>")
