# Generated by Django 3.2.1 on 2021-05-17 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_upvoted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.TextField(blank=True),
        ),
    ]
