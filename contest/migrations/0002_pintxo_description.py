# Generated by Django 4.2.5 on 2023-09-26 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pintxo',
            name='description',
            field=models.TextField(blank=True, max_length=2048, null=True),
        ),
    ]
