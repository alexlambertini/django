# Generated by Django 2.0.6 on 2018-06-22 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='clientes_fotos'),
        ),
    ]
