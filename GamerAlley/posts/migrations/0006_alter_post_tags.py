# Generated by Django 3.2.1 on 2021-05-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.TextField(blank=True),
        ),
    ]
