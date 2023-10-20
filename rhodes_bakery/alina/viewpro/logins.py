from django.shortcuts import render, HttpResponse
from alina.utils.forms import LoginMForm
from alina.models import Login
from django.core.exceptions import ValidationError


def login_list(request):
    query_obj = Login.objects.all()
    print(query_obj[0].username)
    return render(request, 'alina/login_list.html', {"query_obj": query_obj})


def register(request):
    if request.method == "GET":
        form = LoginMForm()
        return render(request, "alina/register.html", {"form": form})
    form = LoginMForm(data=request.POST)

    if form.is_valid():
        user = form.cleaned_data.get('username')
        print(user)
        if Login.objects.filter(username=user).exists():
            # raise ValidationError("user has already in!")
            form.add_error('username', "user has already in!")
            return render(request, "alina/register.html", {"form": form})
        # form.save()
        else:
            print(form.cleaned_data)
            return HttpResponse("success")

    print(form.errors)
    return render(request, "alina/register.html", {"form": form})


def logins(request):
    if request.method == "GET":
        form = LoginMForm()
        return render(request, "alina/logins.html", {"form": form})
