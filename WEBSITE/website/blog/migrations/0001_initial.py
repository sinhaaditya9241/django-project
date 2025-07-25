# Generated by Django 5.2.1 on 2025-05-31 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('public_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
            ],
        ),
    ]
