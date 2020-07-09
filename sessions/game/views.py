from random import randint as random

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

from game.models import Player, Game


def show_home(request):
    print(request.session.items())
    somevalue = True
    context = {"game_id": cache.get("open_game_id"), "keyword": "Загадать"}
    print(cache.get("open_game_id"))
    if cache.get("open_game_id") is None:
        if request.method == "POST":
            if not request.session.get("game_id", None):
                user = Player.objects.create(attempts=0)
                user.save()
                game = Game.objects.create(number=int(request.POST["number"]), master=user)
                game.save()
                cache.set("open_game_id", game.id)
                request.session["game_id"] = game.id
                request.session["player_id"] = user.id
                context["keyword"] = "Проверить"
                somevalue = False
    else:
        if not request.session.get("player_id"):
            user = Player.objects.create(attempts=0)
            user.save()
            request.session["player_id"] = user.id
        context["keyword"] = "Проверить"
        user = Player.objects.filter(id=request.session["player_id"])[0]
        game = Game.objects.filter(id=cache.get("open_game_id"))[0]
        request.session["game_id"] = game.id
        cache.set("open_game_id", None)
        request.session["player_id"] = user.id
        somevalue = False
    print(somevalue)
    if somevalue:
        if request.method == "POST":
            if request.session.get("game_id"):
                game_object = Game.objects.filter(id=request.session.get("game_id"))[0]
                if request.session.get("player_id") == game_object.master_id:
                    pass
                else:
                    if request.POST["number"] != game_object.number:
                        context["is_more"] = True if request.POST["number"] > game_object.number else False
                    else:
                        context["winner"] = True

    return render(
        request,
        'home.html',
        context
    )


def test_view(request):
    context = {
        "keyword": "Проверить"
    }
    if request.session.get("player_id", None):  # Если пользователь имеет сессию(И игру)
        print(request.session["player_id"])
        print("u a have session")
        print(Player.objects.filter(id=request.session["player_id"])[0].master.all())
        print(Player.objects.filter(id=request.session["player_id"])[0].player.all())
        if Player.objects.filter(id=request.session["player_id"])[0].player.all():
            context["is_master"] = False
            if request.method == "POST":
                game_object = Player.objects.filter(id=request.session["player_id"])[0].player.all()[0]
                if int(request.POST["number"]) != game_object.number:
                    context["is_more"] = True if int(request.POST["number"]) > game_object.number else False
                    attempts = Player.objects.filter(id=request.session["player_id"])[0].attempts
                    player = Player.objects.filter(id=request.session["player_id"])[0]

                    player.attempts = attempts + 1

                    player.save()
                    print(attempts)
                else:
                    context["winner"] = True
                    game = Player.objects.filter(id=request.session["player_id"])[0].player.all()[0]
                    game.is_winned = True
                    game.save()
                print(game_object.number)
        else:
            context["is_master"] = True
            if Player.objects.filter(id=request.session["player_id"])[0].master.all()[0].is_winned:
                context["master_lose"] = True
                context["attempts"] = Player.objects.filter(id=request.session["player_id"])[0].master.all()[0].player.attempts



    else:  # Если пользователь без сессии(И игры)
        print("u a haven't session")
        user = Player.objects.create(attempts=0)
        user.save()
        if Game.objects.filter(is_closed=False):
            game = Game.objects.filter(is_closed=False)[0]
            game.player = user
            game.is_closed = True
            game.save()
            request.session["player_id"] = user.id
            print(user.player)
            print("Game linked")
        else:
            game = Game.objects.create(is_closed=False, master=user, number=random(0, 1000))
            request.session["player_id"] = user.id
            game.save()
            print("Game created")

    return render(
        request,
        "home.html",
        context
    )


def create_game(request):
    game = Game.objects.create(is_closed=False, number=10)
    game.save()
    return HttpResponse("SOMETEXTagain")


def clear_games(request):
    for game in Game.objects.filter(is_closed=False):
        game.is_closed = True
        game.save()
    return HttpResponse("SOMETEXTagainagain")


def get_game_id(request):
    return HttpResponse(Player.objects.filter(id=request.session["player_id"])[0].player)
