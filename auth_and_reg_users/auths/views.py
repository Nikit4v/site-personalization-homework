from django.shortcuts import render, redirect

from auths.models import User

from auths.forms import SignUpForm


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
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(request.POST["login"], request.POST["email"], request.POST["password"])
                user.save()
                return redirect("/")
            else:
                context = {
                    "error": True
                }
        else:
            context = {
                "error": True
            }
    context["form"] = SignUpForm()
    return render(
        request,
        'signup.html',
        context
    )
