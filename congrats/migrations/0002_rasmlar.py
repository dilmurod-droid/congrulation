# Generated by Django 5.1.3 on 2025-01-28 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congrats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rasmlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='rasmlar/')),
            ],
        ),
    ]
