# Generated by Django 3.2.1 on 2021-05-12 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodkart', '0009_addresses'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresses',
            name='address',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
