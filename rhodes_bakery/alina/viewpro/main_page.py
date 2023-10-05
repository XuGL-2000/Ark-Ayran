from django.shortcuts import render, HttpResponse


def mian_page(request):
    return render(request, "alina/base.html")
