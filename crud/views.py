from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import UserData
from django.contrib import messages


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

        UserData.objects.create(name=nm, email=email, phone=phone)
        messages.success(req, "Data saved successfully!")

    return render(req, "add-data.html")
