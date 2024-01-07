from django.shortcuts import render


def production(request):
    return render(request, "catalog/production.html")
