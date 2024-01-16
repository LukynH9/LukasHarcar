# Generated by Django 4.2.7 on 2024-01-16 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='polls',
            name='color',
            field=models.CharField(default='x', max_length=200),
        ),
        migrations.AddField(
            model_name='polls',
            name='name',
            field=models.CharField(default='x', max_length=200),
        ),
        migrations.AddField(
            model_name='polls',
            name='url',
            field=models.URLField(default='x'),
        ),
    ]
