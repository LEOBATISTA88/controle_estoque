# Generated by Django 5.0.4 on 2024-05-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_controle_estoque', '0002_item_delete_itens'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='unidade',
            field=models.TextField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='validade',
            field=models.TextField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]