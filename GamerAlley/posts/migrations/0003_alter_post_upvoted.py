# Generated by Django 3.2.1 on 2021-05-17 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_relationship'),
        ('posts', '0002_auto_20210512_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upvoted',
            field=models.ManyToManyField(blank=True, related_name='upvotes', to='profiles.Profile'),
        ),
    ]
