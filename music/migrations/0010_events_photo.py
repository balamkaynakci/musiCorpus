# Generated by Django 4.0.5 on 2022-07-23 10:48

from django.db import migrations, models

from ..models import Events


class Migration(migrations.Migration):

    dependencies = [
        ("music", "0009_rename_name_badge_badge_type_badge_playlist_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="events",
            name="photo",
            field=models.CharField(max_length=255, null=True),
        )
    ]
