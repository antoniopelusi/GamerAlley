# Generated by Django 3.2.1 on 2021-05-18 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(choices=[('adventure', 'adventure'), ('arcade', 'arcade'), ('battleroyale', 'battleroyale'), ('fps', 'fps'), ('mmorpg', 'mmorpg'), ('moba', 'moba'), ('rpg', 'rpg'), ('sandbox', 'sandbox'), ('shooter', 'shooter'), ('simulator', 'simulator'), ('sport', 'sport'), ('survival', 'survival'), ('tactical', 'tactical'), ('other', 'other')], default='adventure', max_length=20),
        ),
    ]
