# Generated by Django 4.0.3 on 2022-03-23 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_alter_contato_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
    ]
