from django.shortcuts import render, redirect

from auths.models import User


def home(request):
    context = {"is_login": request.user.is_authenticated}
    if request.user.is_authenticated:
        context["username"] = request.user.username
    return render(
        request,
        'home.html',
        context
    )


def signup(request):
    context = {
        "error": False
    }
    if request.POST:
        if request.POST["password"] == request.POST["confirm"]:
            user = User.objects.create_user(request.POST["login"], request.POST["email"], request.POST["password"])
            user.save()
            print(request.POST)
            print(user)
            return redirect("/")
        else:
            context = {
                "error": True
            }
    return render(
        request,
        'signup.html',
        context
    )