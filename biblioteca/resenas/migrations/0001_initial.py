# Generated by Django 3.2.5 on 2021-07-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del editorial', max_length=100)),
                ('pagina_web', models.URLField(help_text='Sitio web')),
                ('email', models.EmailField(help_text='Correo electronico', max_length=254)),
            ],
        ),
    ]
