# Generated by Django 4.0.5 on 2022-06-24 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_task_delete_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterModelTable(
            name='task',
            table='webapp_task',
        ),
    ]