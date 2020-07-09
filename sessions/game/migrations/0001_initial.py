# Generated by Django 3.0.7 on 2020-06-27 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.IntegerField()),
                ('session_id', models.TextField()),
                ('attempts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGameInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('is_closed', models.BooleanField()),
                ('master', models.ManyToManyField(related_name='master', to='game.Player')),
                ('players', models.ManyToManyField(related_name='players', to='game.Player')),
            ],
        ),
    ]
