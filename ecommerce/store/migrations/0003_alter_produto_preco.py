# Generated by Django 4.2.2 on 2023-07-15 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
