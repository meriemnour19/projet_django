# Generated by Django 5.0.4 on 2024-04-20 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
