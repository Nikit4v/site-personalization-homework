from django.db import models


class Player(models.Model):
    attempts = models.IntegerField(default=0, blank=True)


class Game(models.Model):
    number = models.IntegerField(blank=True)
    player = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="player", blank=True, null=True)
    master = models.ForeignKey("Player", on_delete=models.CASCADE, related_name="master", blank=True, null=True)
    is_closed = models.BooleanField()


class PlayerGameInfo(models.Model):
    pass
