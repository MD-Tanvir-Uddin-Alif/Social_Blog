# Generated by Django 5.0.6 on 2024-09-19 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_post_model_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_model',
            old_name='like',
            new_name='likes',
        ),
    ]
