from django.shortcuts import render


def contacts(request):
    return render(request, "about/contacts.html")


def factory(request):
    return render(request, "about/factory.html")


def information(request):
    return render(request, "about/information.html")


def map(request):
    return render(request, "about/map.html")
