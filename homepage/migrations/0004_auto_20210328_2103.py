# Generated by Django 3.1.7 on 2021-03-28 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_delete_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.TextField(),
        ),
    ]
