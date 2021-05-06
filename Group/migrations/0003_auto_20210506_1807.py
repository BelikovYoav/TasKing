# Generated by Django 3.2.2 on 2021-05-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0002_alter_group_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(default='NoName', max_length=20),
        ),
        migrations.AlterField(
            model_name='group',
            name='about',
            field=models.TextField(blank=True),
        ),
    ]
