# Generated by Django 3.2.8 on 2023-10-01 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen')),
                ('descripcion', models.TextField(null=True, verbose_name='descripcion')),
            ],
        ),
    ]