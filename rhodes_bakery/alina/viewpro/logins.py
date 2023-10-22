from django.shortcuts import render, HttpResponse, redirect
from alina.utils.forms import LoginMForm
from alina.models import Login
from django.core.exceptions import ValidationError


def login_list(request):
    none_to_show = True

    query_obj = Login.objects.all()
    if len(query_obj) == 0:
        none_to_show = False

    return render(request, 'alina/login_list.html', {"query_obj": query_obj,
                                                     "none_to_show": none_to_show})


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
            form.save()
            print(form.cleaned_data)
            return redirect("/alina/login/list/")

    print(form.errors)
    return render(request, "alina/register.html", {"form": form})


def logins(request):
    if request.method == "GET":
        form = LoginMForm()
        return render(request, "alina/logins.html", {"form": form})


def login_edit(request, nid):
    query_obj = Login.objects.filter(id=nid).first()
    print(query_obj)
    if request.method == "GET":
        form = LoginMForm(instance=query_obj)
        return render(request, "alina/alina_edit.html", {"form": form})
    form = LoginMForm(data=request.POST, instance=query_obj)

    if form.is_valid():
        if Login.objects.filter(username=query_obj.username).exists():
            # raise ValidationError("user has already in!")
            form.add_error('username', "user has already in!")
            return render(request, "alina/alina_edit.html", {"form": form})
        else:
            form.save()
            return redirect("/alina/login/list/")


def login_delete(request, nid):
    Login.objects.filter(id=nid).delete()
    return redirect("/alina/login/list/")
