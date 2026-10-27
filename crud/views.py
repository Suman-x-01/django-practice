from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def home(req):
    return render(req, "index.html")


def service(req):
    return render(req, "service.html")


def contact(req):
    return render(req, "contact.html")
