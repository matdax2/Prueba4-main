# Generated by Django 5.0.4 on 2024-05-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimerApp', '0002_delete_entregable_delete_estudiante_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
