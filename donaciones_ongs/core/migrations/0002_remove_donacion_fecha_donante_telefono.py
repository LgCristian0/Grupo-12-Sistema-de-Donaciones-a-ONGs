# Generated by Django 5.2.1 on 2025-06-04 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donacion',
            name='fecha',
        ),
        migrations.AddField(
            model_name='donante',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
