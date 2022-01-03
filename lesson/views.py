from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.


def index(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username") 
            password = request.POST.get("password")
            user = User.objects.create_user(
                username=username, password=password)
            return render(request, "lesson/user.html", {
                "user": user
            })
        except ValueError:
            return render(request, "lesson/index.html", {
                "message": "Username and Password can't be empty.!!"
            })

    return render(request, "lesson/index.html")

'''def index(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(
            request, username=username, password=password
        )

        if user is not None:
            login(request, user)
            return render(request, "lesson/user.html", {
                "username": username
            })
        else:
            return render(request, "lesson/index.html", {
                "message": "Invalid Credentetials"
            })

    return render(request, "lesson/index.html")
'''
