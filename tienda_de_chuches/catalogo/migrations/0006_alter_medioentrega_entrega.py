# Generated by Django 4.1.11 on 2023-10-22 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_alter_medioentrega_entrega_alter_medioentrega_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medioentrega',
            name='entrega',
            field=models.CharField(max_length=1000),
        ),
    ]