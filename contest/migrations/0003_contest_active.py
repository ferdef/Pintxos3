# Generated by Django 4.2.5 on 2023-10-09 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_pintxo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active?'),
        ),
    ]