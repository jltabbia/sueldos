# Generated by Django 4.2.6 on 2023-10-09 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=10, unique=True, verbose_name='Nombre de Usuario')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Correo Electrónico')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre')),
                ('apellidos', models.CharField(blank=True, max_length=100, null=True, verbose_name='Apellidos')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_administrador', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
    ]
