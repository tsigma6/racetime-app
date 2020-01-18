# Generated by Django 3.0.1 on 2020-01-15 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racetime', '0004_auto_20200115_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='allow_non_entrant_chat',
            field=models.BooleanField(default=True, help_text='Allow users who are not entered in the race to chat while the race is in progress (anyone may use chat before and after the race).'),
        ),
    ]
