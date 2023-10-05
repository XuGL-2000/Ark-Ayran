from django.shortcuts import render, HttpResponse
from alina.utils.forms import LoginMForm


def register(request):
    if request.method == "GET":
        form = LoginMForm()
        return render(request, "alina/register.html", {"form": form})
    form = LoginMForm(data=request.POST)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
        return HttpResponse("success")
    print(form.errors)
    return render(request, "alina/register.html", {"form": form})


def logins(request):
    if request.method == "GET":
        form = LoginMForm()
        return render(request, "alina/logins.html", {"form": form})
