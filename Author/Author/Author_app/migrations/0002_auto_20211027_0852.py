# Generated by Django 2.2.4 on 2021-10-27 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Author_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='notes',
            new_name='author_notes',
        ),
    ]
