# Generated by Django 2.0.6 on 2018-06-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='texto',
            field=models.TextField(max_length=200),
        ),
    ]
