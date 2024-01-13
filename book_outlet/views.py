from django.shortcuts import render
from django.http import HttpResponse


user = {
    "name": "Danny Duong",
    'job': "Software Engineer",
    'address': "Viet Nam"
}


# Create your views here.
def index(request):
    return render(request, "index.html", {
        "data": user
    })