from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from .models import Creature

import re
name_regex = re.compile(r'^[a-zA-Z\s]+$')

def home(request):
    return render(request, "home.html")

def create(request):
    e = []
    if request.method == "POST":
        name = request.POST["name"]
        gender = request.POST["gender"]
        image = request.POST["image"]
        species = request.POST["species"]

        if len(name) < 2:
            e.append("Name must be at least 2 characters long")
            return HttpResponse(e, content_type = "application/json")
        elif not name_regex.match(name):
            e.append("Name must contain only letters and spaces")
            return HttpResponse(e, content_type = "application/json")
        else:
            Creature.objects.create(name = name, gender = gender, image = image, species = species)
            return redirect("/all")

def all(request):
    return render(request, "creatures.html", {"creatures": Creature.objects.all()})

def first(request, num):
    n = int (num)
    if n < 0:
        return redirect("/all")
    else:
        firstNum = Creature.objects.all().order_by("id")[:n]
        return render(request, "creatures.html", {"creatures": firstNum})

def onecreature(request, num):
    return render(request, "info.html", {"creature": Creature.objects.get(id = num)})

def edit(request, num):
    c = Creature.objects.get(id = num)
    e = []

    if request.method == "POST":
        name = request.POST["name"]
        gender = request.POST["gender"]
        image = request.POST["image"]
        species = request.POST["species"]

        if len(name) < 2:
            e.append("Name must be at least 2 characters long")
            return HttpResponse(e, content_type = "application/json")
        elif not name_regex.match(name):
            e.append("Name must contain only letters and spaces")
            return HttpResponse(e, content_type = "application/json")
        else:
            c.name = name
            c.gender = gender
            c.image = image
            c.species = species
            c.save()
            return redirect("/creature/" + num)

def delete(request, num):
    Creature.objects.get(id = num).delete()
    return redirect("/all")

def deletetwo(request, num):
    Creature.objects.get(id = num).delete()
    return redirect("/")

def search(request):
    return render(request, "search.html")

def alltwo(request):
    return render(request, "searchresults.html", {"creatures": Creature.objects.all()})

def searchresults(request):
    return render(request, "searchresults.html", 
    {"creatures": Creature.objects.filter(name__icontains = request.POST["name"])})