# Generated by Django 3.2.1 on 2021-05-17 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(choices=[('adventure', 'ADVENTURE'), ('arcade', 'ARCADE'), ('battle royale', 'BATTLE ROYALE'), ('fps', 'FPS'), ('mmorpg', 'MMORPG'), ('moba', 'MOBA'), ('rpg', 'RPG'), ('sandbox', 'SANDBOX'), ('shooter', 'SHOOTER'), ('simulator', 'SIMULATOR'), ('sport', 'SPORT'), ('survival', 'SURVIVAL'), ('tactical', 'TACTICAL'), ('other', 'OTHER')], default='adventure', max_length=20),
        ),
    ]