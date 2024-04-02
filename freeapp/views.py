from django.shortcuts import render, HttpResponse, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from .forms import LoginForm

from django.contrib.auth.decorators import login_required

from .models import Record

# Create your views here.
# from django.http import HttpResponse


def home(request):
    # return HttpResponse("Hello king")
    return render(request, "freeapp/index.html")


# register
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
    context = {"form": form}

    return render(request, "freeapp/register.html", context=context)


# def register(request):
#     if request.method == "POST":
#         form = CreateUserForm()
#     else:
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse(request, "freeapp/register.html"))

#     context = {"form", form}
#     return render(request, "freeapp/register.html", context)

# login a user


def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")

    context = {"form": form}

    return render(request, "freeapp/my-login.html", context=context)


# Dashboard
@login_required(login_url="my-login")
def dashboard(request):
    my_records = Record.objects.all()

    context = {"records": my_records}

    return render(request, "freeapp/dashboard.html", context=context)


# create record / add


@login_required(login_url="my-login")
def create_record(request):
    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {"form": form}
    return render(request, "freeapp/create-record.html", context=context)


# update record


@login_required(login_url="my-login")
def update_record(request, pk):
    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {"form": form}
    return render(request, "freeapp/update-record.html", context=context)


# read / view singular record


@login_required(login_url="my-login")
def singular_record(request, pk):
    all_records = Record.objects.get(id=pk)

    context = {"record": all_records}

    return render(request, "freeapp/view-record.html", context=context)


# user logout


def user_logout(request):
    auth.logout(request)

    return redirect("my-login")


# delete


@login_required(login_url="my-login")
def delete_record(request, pk):
    record = Record.objects.get(id=pk)

    record.delete()

    return redirect("dashboard")
