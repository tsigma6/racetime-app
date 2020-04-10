# Generated by Django 3.0.2 on 2020-04-08 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racetime', '0026_auto_20200407_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='show_supporter',
            field=models.BooleanField(default=True, help_text='Display your name in a special colour to indicate your support. Turn this off if you would rather stick with the standard name colour.', verbose_name='Use supporter style'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_supporter',
            field=models.BooleanField(default=False, help_text="User has supporter status, indicating they're awesome."),
        ),
    ]