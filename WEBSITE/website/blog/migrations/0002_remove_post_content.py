# Generated by Django 5.2.1 on 2025-05-31 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]
