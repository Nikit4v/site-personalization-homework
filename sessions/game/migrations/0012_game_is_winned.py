# Generated by Django 3.0.7 on 2020-07-09 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_auto_20200709_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_winned',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
