from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def home(req):
    return render(req, "index.html")


def service(req):
    return render(req, "service.html")


def contact(req):
    return render(req, "contact.html")


def add_data(req):
    if req.method == "POST":
        nm = req.POST["name"]
        email = req.POST["email"]
        phone = req.POST["phone"]
        print(nm, email, phone)

    return render(req, "add-data.html")
