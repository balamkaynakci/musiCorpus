# Generated by Django 4.0.5 on 2022-07-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_alter_access_token_access_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlists',
            name='photo_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]