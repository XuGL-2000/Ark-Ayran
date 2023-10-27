from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

from alina.utils.forms import LoginMForm, LoginEditNameForm, LoginEditForm, LoginInForm
from alina.models import Login
from django.core.exceptions import ValidationError


def login_list(request):
    none_to_show = True
    info = request.session.get('info')
    if not info:
        request.session['info'] = {
            "id": None,
            "user": "登录"
        }
    query_obj = Login.objects.all()
    if len(query_obj) == 0:
        none_to_show = False
    return render(request, 'alina/login_list.html', {"query_obj": query_obj,
                                                     "none_to_show": none_to_show, })


def login_add(request):
    if request.method == "GET":
        form = LoginMForm()
        return render(request, "alina/login_add.html", {"form": form})
    form = LoginMForm(data=request.POST)

    if form.is_valid():
        user = form.cleaned_data.get('username')
        # print(user)
        if Login.objects.filter(username=user).exists():
            # raise ValidationError("user has already in!")
            form.add_error('username', "user has already in!")
            return render(request, "alina/login_add.html", {"form": form})
        # form.save()
        else:
            form.save()
            # print(form.cleaned_data)
            return redirect("/alina/login/list/")

    print(form.errors)
    return render(request, "alina/login_add.html", {"form": form})


def logins(request):
    if request.method == "GET":
        form = LoginInForm()
        return render(request, "alina/logins.html", {"form": form})
    form = LoginInForm(data=request.POST)
    print(request.POST)
    if form.is_valid():
        login_object = Login.objects.filter(**form.cleaned_data).first()
        if not login_object:
            form.add_error("password", "用户名或密码不正确！")
        request.session['info'] = {"id": login_object.id,
                                   "user": login_object.username}
        request.session.set_expiry(60 * 60 * 24 * 7)
        print(request.session['info'])
        return JsonResponse({'status': True})

    return JsonResponse({'status': False, 'errors': form.errors})


def login_out(request):
    request.session.clear()
    return redirect("/alina/login/list/")


def login_edit(request, nid):
    # query_obj = Login.objects.filter(id=nid).first()
    # print(query_obj)
    # if request.method == "GET":
    #     form = LoginMForm(instance=query_obj)
    #     return render(request, "alina/alina_edit.html", {"form": form})
    # form = LoginMForm(data=request.POST, instance=query_obj)
    #
    # if form.is_valid():
    #     if Login.objects.exclude(username=query_obj.username).filter(username=form.cleaned_data['username']).exists():
    #         # raise ValidationError("user has already in!")
    #         form.add_error('username', "user has already in!")
    #         return render(request, "alina/alina_edit.html", {"form": form})
    #     else:
    #         form.save()
    #         return redirect("/alina/login/list/")
    # return render(request, "alina/alina_edit.html", {"form": form})
    query_obj = Login.objects.filter(id=nid).first()
    print(query_obj)
    if request.method == "GET":
        form = LoginEditForm()
        return render(request, "alina/login_edit_password.html", {"query_obj": form})
    print(request.POST)
    form = LoginEditForm(data=request.POST, instance=query_obj)
    if form.is_valid():
        if request.POST["password"] == query_obj.password:
            form.add_error("password", "password can't be same with before")
            return render(request, "alina/login_edit_password.html", {"query_obj": form})
        else:
            form.save()
            return redirect("/alina/login/list/")

    return render(request, "alina/login_edit_password.html", {"query_obj": form})


# @csrf_exempt
def login_edit_name(request):
    nid = request.GET.get('nid')
    query_obj1 = Login.objects.filter(id=nid).first()
    users = query_obj1.username
    form = LoginEditNameForm(data=request.POST, instance=query_obj1)
    print("ew", request.POST)
    print(query_obj1)
    if form.is_valid():
        print(query_obj1)
        bools = Login.objects.exclude(username=users).filter(username=request.POST['username']).exists()
        print(query_obj1.username, request.POST['username'])
        print(users)
        print(bools)
        if bools:
            form.add_error('username', 'user has already in!')
            return JsonResponse({'status': False, 'errors': form.errors})
        else:
            form.save()
            return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'errors': form.errors})


def login_delete(request, nid):
    Login.objects.filter(id=nid).delete()
    return redirect("/alina/login/list/")
