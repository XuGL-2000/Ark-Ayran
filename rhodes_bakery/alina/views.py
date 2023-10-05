from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def redirs(request):
    return redirect("/alina/m_page/")


def hello(request):
    return HttpResponse("罗德岛蜜饼工坊-Ayran")
