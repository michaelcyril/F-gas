# Generated by Django 4.2.1 on 2023-06-04 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authUser', '0002_remove_user_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
