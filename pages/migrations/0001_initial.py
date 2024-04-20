# Generated by Django 5.0.4 on 2024-04-20 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='announce/%y/%m/%d')),
                ('title', models.CharField(max_length=100)),
                ('launching_date', models.DateField()),
                ('content', models.TextField()),
                ('add_date', models.DateField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
